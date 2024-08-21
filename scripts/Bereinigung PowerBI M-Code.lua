let
    // 1. Ausgangsdatenquelle und erste Anpassungen
    Quelle = Csv.Document(File.Contents("C:\Users\HP\OneDrive\Desktop\depression_anxiety_data.csv"),[Delimiter=",", Columns=19, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Höher gestufte Header" = Table.PromoteHeaders(Quelle, [PromoteAllScalars=true]),
    
    // 2. Datentypen und Werteanpassungen
    #"bmi Punkt zu Komma" = Table.ReplaceValue(#"Höher gestufte Header",".",",",Replacer.ReplaceText,{"bmi"}),
    #"Ersetzter Wert" = Table.ReplaceValue(#"bmi Punkt zu Komma","NA","-1",Replacer.ReplaceText,{"epworth_score"}),
    #"Geänderter Typ" = Table.TransformColumnTypes(#"Ersetzter Wert",{{"id", Int64.Type}, {"school_year", Int64.Type}, {"age", Int64.Type}, {"bmi", type number}, {"who_bmi", type text}, {"phq_score", Int64.Type}, {"depression_severity", type text}, {"depressiveness", type text}, {"gad_score", Int64.Type}, {"anxiety_severity", type text}, {"epworth_score", Int64.Type}}),

    // 3. Entfernen der Zeilen mit NA in bestimmten Spalten
    GefilterteZeilen1 = Table.SelectRows(#"Geänderter Typ", each ([suicidal] <> "NA") and 
                                                    ([anxiety_diagnosis] <> "NA") and 
                                                    ([anxiety_treatment] <> "NA") and 
                                                    ([depression_diagnosis] <> "NA") and 
                                                    ([depression_treatment] <> "NA")),

    // 4. Berechnung von Medianwerten für "bmi", "epworth_score", "phq_score" und "gad_score"
    MedianBMI = List.Median(GefilterteZeilen1[bmi]),
    MedianPHQ = List.Median(GefilterteZeilen1[phq_score]),
    MedianEpworth = List.Median(GefilterteZeilen1[epworth_score]),
    MedianGAD = List.Median(GefilterteZeilen1[gad_score]),

    // 5. Bereinigen der "bmi"-Spalte: Ersetzen von 0-Werten durch den Median
    ErsetzterBMI = Table.ReplaceValue(GefilterteZeilen1, 0, MedianBMI, Replacer.ReplaceValue, {"bmi"}),

    // 6. Aktualisieren der "who_bmi"-Spalte, um Fehlzuordnungen zu vermeiden
    EntfernteSpalten = Table.RemoveColumns(ErsetzterBMI, {"who_bmi"}),
    HinzugefügteWHO_BMI = Table.AddColumn(EntfernteSpalten, "who_bmi", each 
        if [bmi] < 18.4 then "Underweight" 
        else if [bmi] < 24.9 then "Normal" 
        else if [bmi] < 29.9 then "Overweight" 
        else if [bmi] < 34.9 then "Class I Obesity" 
        else if [bmi] < 40 then "Class II Obesity" 
        else if [bmi] > 40 then "Class III Obesity" 
        else "NA"),

    // 7. Bereinigen der "epworth_score"-Spalte: Anpassen der Werte
    EpworthBereinigt = Table.ReplaceValue(HinzugefügteWHO_BMI, each [epworth_score], 
                            each if [epworth_score] < 0 then MedianEpworth
                            else if [epworth_score] > 24 and [sleepiness] = "TRUE" then 17
                            else if [epworth_score] > 24 and not [sleepiness] = "TRUE" then MedianEpworth
                            else [epworth_score], 
                            Replacer.ReplaceValue, {"epworth_score"}),

    // 8. Aktualisieren der "sleepiness"-Spalte basierend auf "epworth_score"
    EntfernteSleepiness = Table.RemoveColumns(EpworthBereinigt, {"sleepiness"}),
    HinzugefügteSleepiness = Table.AddColumn(EntfernteSleepiness, "sleepiness", each if [epworth_score] > 9 then true else false),

    // 9. Bereinigen der "gad_score"-bezogenen Spalten
    EntfernteAnxSeverity = Table.RemoveColumns(HinzugefügteSleepiness, {"anxiety_severity"}),
    HinzugefügteAnxSeverity = Table.AddColumn(EntfernteAnxSeverity, "anxiety_severity", each
        if [gad_score] < 4 then "None-minimal"
        else if [gad_score] < 9 then "Mild"
        else if [gad_score] < 14 then "Moderate"
        else if [gad_score] < 21 then "Severe"
        else "NA"),

    EntfernteAnx = Table.RemoveColumns(HinzugefügteAnxSeverity, {"anxiousness"}),
    HinzugefügteAnx = Table.AddColumn(EntfernteAnx, "anxiousness", each
        if [gad_score] <= 9 then "FALSE"
        else "TRUE"),

    // 10. Bereinigen der "phq_score"-bezogenen Spalten
    phq_score_updated = Table.ReplaceValue(HinzugefügteAnx,
        each [phq_score],  
        each if [phq_score] = 0 and [depression_severity] = "NA" then MedianPHQ else [phq_score],
        Replacer.ReplaceValue,
        {"phq_score"}),

    EntfernteDepSeverity = Table.RemoveColumns(phq_score_updated, {"depression_severity"}),
    HinzugefügteDepSeverity = Table.AddColumn(EntfernteDepSeverity, "depression_severity", each 
        if [phq_score] < 4 then "None-minimal" 
        else if [phq_score] < 9 then "Mild" 
        else if [phq_score] < 14 then "Moderate" 
        else if [phq_score] < 19 then "Moderately severe" 
        else if [phq_score] < 27 then "Severe" 
        else "NA"),

    EntfernteDepressiveness = Table.RemoveColumns(HinzugefügteDepSeverity, {"depressiveness"}),
    HinzugefügteDepressiveness = Table.AddColumn(EntfernteDepressiveness, "depressiveness", each
        if [phq_score] < 9 and [suicidal] = "TRUE" then "TRUE"
        else if [phq_score] > 9 then "TRUE"
        else "FALSE"),

    // 11. Neuordnung der Spalten
    NeuAngeordneteSpalten = Table.ReorderColumns(HinzugefügteDepressiveness, 
        {"id", "school_year", "age", "gender", "bmi", "who_bmi", "phq_score", 
         "depression_severity", "depressiveness", "suicidal", 
         "depression_diagnosis", "depression_treatment", "gad_score", 
         "anxiety_severity", "anxiousness", "anxiety_diagnosis", 
         "anxiety_treatment", "epworth_score", "sleepiness"}),

    // 12. Typanpassungen (einschließlich der ersetzten Spalten)
    GeänderterTypFinal = Table.TransformColumnTypes(NeuAngeordneteSpalten,
        {{"id", Int64.Type}, {"school_year", Int64.Type}, {"age", Int64.Type}, 
         {"bmi", type number}, {"who_bmi", type text}, {"phq_score", Int64.Type}, 
         {"depression_severity", type text}, {"depressiveness", type text}, 
         {"gad_score", Int64.Type}, {"anxiety_severity", type text}, 
         {"epworth_score", Int64.Type}, {"sleepiness", type logical}, 
         {"anxiety_treatment", type logical}, {"anxiety_diagnosis", type logical}, 
         {"anxiousness", type logical}, {"depression_treatment", type logical}, 
         {"depression_diagnosis", type logical}, {"suicidal", type logical}})
        
in
    GeänderterTypFinal
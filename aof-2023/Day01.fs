module Day01

open System
open System.IO

let combineFirstAndLastNum =
    Seq.toList
    >> Seq.filter Char.IsDigit
    >> (fun ary -> (Char.ToString (Seq.head ary)) + (Char.ToString (Seq.last ary)))
    >> Int32.Parse

let part01 =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day01_part02.txt"))
    |> Seq.map combineFirstAndLastNum
    |> Seq.sum
    
let nameNumberMap = Map[
    ("one", "1")
    ("two", "2")
    ("three", "3")
    ("four", "4")
    ("five", "5")
    ("six", "6")
    ("seven", "7")
    ("eight", "8")
    ("nine", "9")
]

let findNextSpelledNumber (str: String) =
    Map.keys nameNumberMap
    |> Seq.map (fun key -> (key, str.IndexOf key))
    |> Seq.sortBy snd
    |> Seq.filter (fun (_, i) -> i >= 0)
    |> Seq.toList
    |> function
        | [] -> None
        | x::_ -> Some (fst x)
    
let rec replaceNamesWithNumbers str =
    findNextSpelledNumber str
    |> function
        | None -> str
        | Some(name) -> replaceNamesWithNumbers (str.Replace (name, nameNumberMap[name]))

let part02 =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day01_part02.txt"))
    |> Seq.map replaceNamesWithNumbers
    |> Seq.map combineFirstAndLastNum
    |> Seq.sum

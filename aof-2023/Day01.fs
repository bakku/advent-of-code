module Day01

open System
open System.IO
open System.Text.RegularExpressions

let combineFirstAndLastNum =
    Seq.toList
    >> Seq.filter Char.IsDigit
    >> (fun ary -> (Char.ToString (Seq.head ary)) + (Char.ToString (Seq.last ary)))
    >> Int32.Parse

let part01 =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day01_part01.txt"))
    |> Seq.map combineFirstAndLastNum
    |> Seq.sum
    
let nameNumberMap = Map[
    ("one", 1)
    ("two", 2)
    ("three", 3)
    ("four", 4)
    ("five", 5)
    ("six", 6)
    ("seven", 7)
    ("eight", 8)
    ("nine", 9)
    ("1", 1)
    ("2", 2)
    ("3", 3)
    ("4", 4)
    ("5", 5)
    ("6", 6)
    ("7", 7)
    ("8", 8)
    ("9", 9)
]

let allIndexesOf str substr =
    Regex.Matches (str, (Regex.Escape substr))
    |> Seq.map (fun m -> m.Index)
    
let findAllKeyIndexPairs str key =
    allIndexesOf str key
    |> Seq.map (fun idx -> (key, idx))

let findAllNumbers (str: String) =
    Map.keys nameNumberMap
    |> Seq.collect (findAllKeyIndexPairs str)
    |> Seq.filter (fun (_, i) -> i >= 0)
    |> Seq.sortBy snd
    
let findFirstAndLastNumber (str: String) =
    let allNumbers = findAllNumbers str
                     |> Seq.map fst
    
    (Seq.head allNumbers, Seq.last allNumbers)
    
let combineNumberTuple tuple =
    let fstAsString = string nameNumberMap[fst tuple]
    let sndAsString = string nameNumberMap[snd tuple]
    
    Int32.Parse (fstAsString + sndAsString)

let part02 =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day01_part02.txt"))
    |> Seq.map findFirstAndLastNumber
    |> Seq.map combineNumberTuple
    |> Seq.sum

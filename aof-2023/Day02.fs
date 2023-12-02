module Day02

open System
open System.IO
open Microsoft.FSharp.Core

type Color =
    | Red
    | Green
    | Blue

type CubeSet =
    { Amount: int; Color: Color }
type CubeDraw = CubeSet list
type Game =
    { Id: int; Draws: CubeDraw list }

let parseColor = function
    | "green" -> Green
    | "red" -> Red
    | _ -> Blue

let parseCubeSet (cubeSet: string) =
    match cubeSet.Split(" ") with
    | [|amountStr; colorStr|] -> Some { Amount = Int32.Parse amountStr; Color = parseColor colorStr }
    | _ -> None

let parseCubeDraw (cubeDraw: string) =
    cubeDraw.Split(", ")
    |> Seq.map parseCubeSet
    |> Seq.choose id
    |> Seq.toList

let parseDraws (str: string) =
    str.Split("; ")
    |> Seq.map parseCubeDraw
    |> Seq.toList

let parseGame (game: string) =
    match (game.Split("Game ")[1]).Split(": ") with
    | [|idAsStr; drawsAsStr|] -> Some { Id = Int32.Parse idAsStr; Draws = parseDraws drawsAsStr }
    | _ -> None

let parseGames input =
    input
    |> Seq.map parseGame
    |> Seq.choose id

let maxRedCubes = 12
let maxGreenCubes = 13
let maxBlueCubes = 14

let doesDrawExceedMaxCubesForColor draw color maxAmount =
    match (List.tryFind (fun c -> c.Color = color) draw) with
                        | Some c -> c.Amount > maxAmount
                        | None -> false

let doesDrawExceedMaxCubes (draw: CubeDraw) =
    doesDrawExceedMaxCubesForColor draw Red maxRedCubes
    || doesDrawExceedMaxCubesForColor draw Green maxGreenCubes
    || doesDrawExceedMaxCubesForColor draw Blue maxBlueCubes

let isPossibleGame (game: Game) =
    (List.exists doesDrawExceedMaxCubes game.Draws) = false
    
let part01Input =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day02_part01.txt"))

let part01 =
    parseGames part01Input
    |> Seq.filter isPossibleGame
    |> Seq.sumBy (fun g -> g.Id)

let maxCubeSetAmountForColor cubeSets color =
    cubeSets
    |> List.filter (fun c -> c.Color = color)
    |> List.map (fun c -> c.Amount)
    |> List.max
                      
let powerOfMinCubeSet game =
    let cubeSets = List.collect id game.Draws
    
    maxCubeSetAmountForColor cubeSets Red
    * maxCubeSetAmountForColor cubeSets Green
    * maxCubeSetAmountForColor cubeSets Blue
    
let part02Input =
    File.ReadLines (Path.Combine (__SOURCE_DIRECTORY__, "input", "day02_part02.txt"))

let part02 =
    parseGames part02Input
    |> Seq.map powerOfMinCubeSet
    |> Seq.sum

module StringSet = Set.Make (String)

let removed_arr list x = List.filter (fun e -> e <> x) list

let rec candidate_checker (x : string list) (lim : int) (cand : string list)
    (n : int) =
  if n = lim then raise (Failure "Too Many Candidates Ranked")
  else
    match x with
    | [] -> true
    | h :: t ->
        if List.mem h cand then
          candidate_checker t lim (removed_arr cand h) (n + 1)
        else raise (Failure "Ranked a non-existent candidate")

let rec dimension_checker (x : string list list) (cand_size : int)
    (cand : string list) =
  match x with
  | [] -> true
  | h :: t -> (
      try
        let _ = candidate_checker h 0 cand cand_size in
        dimension_checker t cand_size cand
      with Failure msg -> raise (Failure msg))

let rec dimcand_check (x : string list list) (len : int) (set : StringSet.t) =
  match x with
  | [] ->
      if StringSet.cardinal set < len then
        raise (Failure "Duplicate Candidates")
      else StringSet.elements set
  | [] :: t -> dimcand_check t len set
  | [ h ] :: t -> dimcand_check t (len + 1) (StringSet.add h set)
  | _ -> raise (Failure "More than One Candidate in One Line")

let increment (ind : int) (vals : int) (liste : int list) =
  List.mapi (fun i x -> if i = ind then vals + x else x) liste

let rec points (reward : int) (order : string list) (candidates : string list)
    (accume : int list) =
  match order with
  | [] -> accume
  | h :: t ->
      points (reward - 1) t candidates
        (increment
           (Option.get (List.find_index (fun x -> x = h) candidates))
           reward accume)

let rec voting2 (rankings : string list list) (candidates : string list)
    (accum : int list) =
  match rankings with
  | [] -> List.combine candidates accum
  | h :: t ->
      voting2 t candidates
        (points (List.length candidates - 1) h candidates accum)

let rec voting (rankings : string list list) (candidates : string list) =
  try
    let _ = dimension_checker rankings (List.length candidates) candidates in
    voting2 rankings candidates [ 0; 0; 0 ]
  with Failure msg -> raise (Failure msg)

let preferences =
  [
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Chocolate"; "Vanilla"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Strawberry"; "Chocolate"; "Vanilla" ];
    [ "Strawberry"; "Vanilla"; "Chocolate" ];
    [ "Strawberry"; "Chocolate"; "Vanilla" ];
    [ "Strawberry"; "Vanilla"; "Chocolate" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Strawberry"; "Chocolate"; "Vanilla" ];
    [ "Chocolate"; "Vanilla"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Strawberry"; "Chocolate"; "Vanilla" ];
    [ "Chocolate"; "Vanilla"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
    [ "Strawberry"; "Vanilla"; "Chocolate" ];
    [ "Strawberry"; "Chocolate"; "Vanilla" ];
    [ "Chocolate"; "Vanilla"; "Strawberry" ];
    [ "Vanilla"; "Chocolate"; "Strawberry" ];
  ]

let cand = [ "Vanilla"; "Chocolate"; "Strawberry" ]
let x = voting preferences cand
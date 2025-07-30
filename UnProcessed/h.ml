(* let rec rev_map_aux f acc = function
  | [] -> acc
  | h :: t -> rev_map_aux f (f h :: acc) t

let rev_map f = rev_map_aux f []

let lst = rev_map (fun x -> x + 1) [1; 2; 3] *)

let twice f x = f (f x)

let four x = 2 * x
let d = twice four 1



let rec max (list : int list) (maxint : int)= 
  match list with 
  | [] -> maxint
  | h :: t -> if h > maxint then max t h else max t maxint

let list_max (list : int list) = 
  match list with 
  |[] -> raise (Failure "Bruh")
  | h::t -> max t h 



type student = { 
  name: string;
  year: int;
  netid: string;
}



type point = float*float

type color = 
|Point of point
|Circle of {
  center:point;
  radius:float;
}

let h = Circle{center = (1.0,1.0); radius = 1.0}

let centers shape = 
  match shape with
  | Point p -> p 
  | Circle {center} -> center

let reflect shape = 
  match shape with
  | Point (x,y) -> (y,x)
  | Circle {center = x,y} -> (y,x)



let rbg = {
  name = "RBG";
  year = 1954;
  netid = "Z"
}

let x = {rbg with name = "z"}

let name_of_stu' stu = 
  match stu with 
  | { name = n; year = y; netid = id } -> n

(name_of_stu') (rbg);;




type 'a list = 
|Empty
|Node of 'a * 'a list

type 'a ocamllist = 
|[]
|(::) of 'a * 'a ocamllist

let rec length intlist = 
  match intlist with
  |Empty -> 0
  |Node(_,t)-> 1+length t

let ili = Node(1,Node(2,Empty))


(* Define the tree type *)
type 'a tree = 
  | Leaf
  | Node of 'a * 'a tree * 'a tree

(* Function to calculate the size of the tree *)
let rec size = function
  | Leaf -> 0
  | Node (_, lt, rt) -> 1 + size lt + size rt



let rec add1 lst = 
  match lst with
  | [] -> []
  | h :: t -> h+1 :: add1 t


let rec concat_bang lst = 
  match lst with
  | [] -> []
  | h :: t -> (h^"!") :: concat_bang t




let rec transform func lst = 
  match lst with
  | [] -> []
  | h::t -> func h :: transform func t

let add1' = transform (fun x -> x+1)
(* 
add1' ([1;2;3]) *)


let concat_band = transform (fun x -> x ^ "!")

let rec combine init func lst = 
  match lst with
  | [] -> init 
  | h :: t -> func (h) (combine init func t)

let add' = combine 0 ( + )

let add' = combine 0 (fun x -> fun y-> y + x)

let prod = combine 1 (fun x -> fun y-> y * x)

let cocnat = combine "" ( ^ )

let rec fold_right f acc lst = 
  match lst with| [] -> acc
  | h::t -> f h (fold_right f acc t)

let rec fold_left f acc lst = 
  match lst with
  | [] -> acc
  | h::t -> fold_left f (f acc h) t

let rec filter judge lst = 
  match lst with
  | [] -> []
  | h::t -> if judge h then h::filter judge t else filter judge t



(* fold_left is tail recursive, fold_right needs to be commutative and associative *)

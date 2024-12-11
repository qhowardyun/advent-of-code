open Printf

let id x = x
let tuple x y = (x,y)

let line_stream_of_channel : 'a -> string Stream.t =
 fun channel ->
  let read () = input_line channel in
  Stream.from (fun _ -> try Some (read ()) with End_of_file -> Option.None)

let get_lines ?on_eof day parse_line =
  let lines = ref [] in
  let in_channel = open_in ((string_of_int day) ^ ".in") in
  try
    Stream.iter
      (fun line -> lines := parse_line line :: !lines)
      (line_stream_of_channel in_channel);
    close_in in_channel;
    !lines |> List.rev
  with e ->
    match on_eof with Some f -> f () | _ -> ();
    close_in in_channel;
    raise e

let get_all_lines day = get_lines day (fun f -> f)

let group_by_newline lines =
  List.fold_left
    (fun acc s ->
      match String.trim s with
      | "" -> [] :: acc
      | _ -> (
          match acc with
          | hd :: tail -> (s :: hd) :: tail
          | _ -> failwith @@ sprintf "bad lines %s" s ))
    [ [] ] lines

let get_newline_delimited_lines day = get_lines day (fun i -> i) |> List.rev |> group_by_newline

let test_input = "199
200
208
210
200
207
240
269
260
263"


let rec count_increases acc elems =
  match elems with
  | a :: b :: tail ->
      let acc = if a < b then acc + 1 else acc in
      b :: tail |> count_increases acc
  | _ -> acc;;
let count elems = count_increases 0 elems;;

let part1 input = List.map int_of_string input |> count |> print_int |> print_newline;;

let solvep1 = part1 (get_all_lines 1);;

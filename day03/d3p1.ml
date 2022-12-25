let score = 0
let characters = Hashtbl.create 1000
  
let base = Char.code 'A' - 27;;
for i = 27 to 52 do
  let c = Char.chr (i + base) in
  Hashtbl.add characters c i
done

let base = Char.code 'a' - 1;;
for i = 1 to 26 do
  let c = Char.chr (i + base) in
  Hashtbl.add characters c i
done
  





let file = open_in "input.txt";;
try
  while true do
    let 
      line = input_line file
    in
      {
      for c = 0 to ((String.length line)/2 - 1) do
        let bag_one = Hashtbl.create 1000
        Hashtbl.add bag_one line.[c] 1
      done
      for c = ((String.length line)/2) to (String.length line - 1) do
        if Hashtbl.mem bag_one line.[c] then
          score = score + (Hashtbl.find characters line.[c])
      done
      }
  done
with End_of_file ->
  close_in file

print_endline (string_of_int score)
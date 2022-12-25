score :: String -> Int
score match = match[0] + match[2]
score "A X" = 3
score "A Y" = 4
score "A Z" = 8
score "B X" = 1
score "B Y" = 5
score "B Z" = 9
score "C X" = 2
score "C Y" = 6
score "C Z" = 7

read_numbers = do
    contents <- readFile "input.txt"
    -- let linesOfFile = map (\x -> read x :: String) (lines $ contents)
    let linesOfFile = (lines $ contents)
    return linesOfFile

main = do
      xs <- read_numbers
      print (sum (map score xs))
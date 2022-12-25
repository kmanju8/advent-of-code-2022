score :: String -> Int
score "A X" = 4
score "A Y" = 8
score "A Z" = 3
score "B X" = 1
score "B Y" = 5
score "B Z" = 9
score "C X" = 7
score "C Y" = 2
score "C Z" = 6

read_numbers = do
    contents <- readFile "input.txt"
    -- let linesOfFile = map (\x -> read x :: String) (lines $ contents)
    let linesOfFile = (lines $ contents)
    return linesOfFile

main = do
      xs <- read_numbers
      print (sum (map score xs))
compareWithHundred :: (Num a, Ord a) => a -> Ordering
compareWithHundred = compare 100 

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: (a -> b -> c) -> b -> a -> c
flip' f y x = f x y

map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x:xs) = f x : Main.map f xs

filter :: (a -> Bool) -> [a] -> [a]
filter _ [] = []
filter p (x:xs)
	| p x = x : Main.filter p xs
	| otherwise = Main.filter p xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
    let smallerSorted = quicksort (Main.filter (<=x) xs)
        biggerSorted = quicksort (Main.filter (>x) xs)
    in smallerSorted ++ [x] ++ biggerSorted

largestDivisible :: (Integral a) => a
largestDivisible = head (Main.filter p [100000,99999..])
	where p x = x `mod` 3829 == 0




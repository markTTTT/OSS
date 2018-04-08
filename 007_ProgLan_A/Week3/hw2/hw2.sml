(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

fun all_except_option(s : string, slist : string list) =
    let fun split_list(s, output, test) =
	    case (s, output, test) of
		(s, _, []) => NONE
	      | (s, _, hd::tl) => if same_string(s, hd)
				  then SOME (output @ tl)
				  else split_list(s, hd::output, tl)
    in split_list(s, [], slist)
    end

fun get_substitutions1(sll : string list list, s : string) =
    case (sll) of
	([[]]) => []
      | (hd::tl) => let val x = all_except_option(s, hd)
			val unoption = case x of
					   NONE => []
					 | SOME x => x
		    in unoption @ get_substitutions1(tl, s) end
      | _ => [] 

fun get_substitutions2(sll : string list list, s : string) =
    let fun aux(sll, sll2, s) =
	    case sll2 of
		[] => sll
	      | hd::tl => let val x = all_except_option(s, hd)
			      val unoption = case x of
						 NONE => [] 
					       | SOME x => x
			  in aux(sll @ unoption, tl, s) end
    in aux([], sll, s) end

fun similar_names(sll : string list list, {first:string, middle:string, last:string}) =
    case (first, middle, last) of
	(a, b, c) => let fun create_names(x, b, c) =
			     case x of
				 [] => []
			       | hd::tl => {first=hd, middle=b, last=c} :: create_names(tl, b, c)
		     in {first=a, middle=b, last=c} :: create_names(get_substitutions2(sll, a), b, c)
		     end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)

fun card_color(suit, rank) =
    case (suit, rank) of
	(Clubs, _) => Black
      | (Spades, _) => Black
      | _ => Red 

fun card_value(suit, rank) =
    case rank of
	Num x => x
      | Ace => 11
      | _ => 10

fun remove_card(cs, c, e) =
    let fun lists(keep, main, c) =
	    case main of
		[] => raise e
	      | hd::tl => if hd = c then keep @ tl
			  else lists(hd::keep, tl, c)
    in lists([], cs, c)
    end

fun all_same_color(clist) =
    case (clist) of
	[] => true
      | _::[] => true
      | (suit1, rank1)::((suit2, rank2)::rest) => card_color(suit1, rank1) = card_color(suit2, rank2)
						  andalso all_same_color((suit2, rank2)::rest)

fun sum_cards(clist) =
    let fun helper(clist, sum) =
	    case clist of
		[] => 0
	      | (suit, rank)::[] => card_value(suit, rank) + sum
	      | (suit, rank)::rest => helper(rest, sum + card_value(suit, rank))
    in helper(clist, 0)
    end

fun score(clist, goal) =
    let val sum = sum_cards(clist)
	fun helper() =
	    if sum > goal then 3 * (sum - goal)
	    else (goal - sum)
    in if all_same_color(clist) then helper() div 2
       else helper()
    end

fun officiate(clist, mlist, goal) =
    let val heldCards = []
	val theScore = 0
(*	val args = (clist, mlist, goal, heldCards, theScore) *)
	fun helper(clist, mlist, goal, heldCards, theScore) =
	    case (clist, mlist, goal, heldCards, theScore) of
		([], _, _, _, theScore) => theScore
	      | (_, [], _, _, theScore) => theScore
	      | (card::tl, move::rest, _, _, _) =>
		let fun moveHelper(mv) = 
			case mv of
			    Discard(suit, rank) => let val newHand = remove_card(heldCards, (suit, rank), IllegalMove)
						   in helper(clist, rest, goal, newHand, score(newHand, goal))
						   end
			  | Draw => if sum_cards(card::heldCards) > goal then score(card::heldCards, goal)
				    else let val newHand = card::heldCards
					 in helper(tl, rest, goal, newHand, score(newHand, goal))
					 end
		in moveHelper(move)
		end
    in helper(clist, mlist, goal, heldCards, theScore)
    end
							



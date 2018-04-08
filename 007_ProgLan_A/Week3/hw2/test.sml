fun same_string(s1 : string, s2 : string) =
    s1 = s2

fun all_except_option(s : string, slist : string list) =
    let fun split_list(s, output, test) =
	    case (s, output, test) of
		(s, _, []) => NONE
	      | (s, _, hd::tl) => if same_string(s, hd)
				  then SOME (output @ tl)
				  else split_list(s, hd::output, tl)
    in split_list(s, [], slist)
    end

fun deoption(opt : string list option) =
    case opt of
	NONE => []
     | SOME opt => opt 

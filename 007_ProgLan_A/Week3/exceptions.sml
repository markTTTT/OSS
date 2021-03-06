fun hd xs =
    case xs of
	[] => raise List.Empty
      | x::_ => x

exception MyUndesirableException
exception MyOtherException of int * int

fun mydiv (x, y) =
    if y=0
    then raise MyUndesirableException
    else x div y

fun maxlist (xs, ex) = (* int list * exn -> int *)
    case xs of
	[] => raise ex
      | x::[] => x
      | x::xs' => Int.max(x, maxlist(xs', ex))

val w = maxlist ([3, 4, 5], MyUndesirableException)
val x = maxlist ([3, 4, 5], MyUndesirableException)
	handle MyUndesirableException => 42

val z = maxlist ([], MyUndesirableException)
		handle MyUndesirableException => 42

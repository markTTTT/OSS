fun is_older (x : int*int*int, y : int*int*int) =
    if #1 x < #1 y then true
    else if #1 x = #1 y
    then if #2 x < #2 y then true
	 else if #2 x = #2 y then #3 x < #3 y
	 else false
    else false

fun number_in_month (dates : (int*int*int) list, x : int) =
    if null (tl dates)
    then if #2 (hd dates) = x
	 then 1 else 0
    else
	if #2 (hd dates) = x
	then 1 + number_in_month(tl dates, x)
	else number_in_month(tl dates, x)

fun number_in_months (dates : (int*int*int) list, months :  int list) =
    if null (tl months)
    then number_in_month(dates, hd months)
    else let val x = number_in_months(dates, tl months)
	 in number_in_month(dates, hd months) + x
	 end

fun dates_in_month (dates : (int*int*int) list, month : int) =
    if null (tl dates)
    then if #2 (hd dates) = month
	 then dates else []
    else
	if #2 (hd dates) = month
	then hd dates :: dates_in_month(tl dates, month)
	else dates_in_month(tl dates, month)

fun dates_in_months (dates : (int*int*int) list, months :  int list) =
    if null (tl months)
    then dates_in_month(dates, hd months)
    else let val x = dates_in_months(dates, tl months)
	 in dates_in_month(dates, hd months) @ x
	 end

fun get_nth (xs : string list, n : int) =
    if n = 1 then hd xs
    else get_nth(tl xs, n-1)

fun date_to_string (date : int*int*int) =
    let
	val month = get_nth(["January","February","March","April","May","June","July","August","September","October","November","December"], #2 date)
	val day = Int.toString(#3 date)
	val year = Int.toString(#1 date)
    in month ^ " " ^ day ^ ", " ^ year
    end

fun number_before_reaching_sum (sum : int, xs : int list) =
    if hd xs < sum andalso (hd xs + hd (tl xs)) >= sum then 1
    else 1 + number_before_reaching_sum(sum-(hd xs), tl xs)

fun what_month (doy : int) =
    let val x = number_before_reaching_sum(doy, [31,28,31,30,31,30,31,31,30,31,30,31])
    in 1 + x end

fun month_range (day1 : int, day2 : int) =
    let val result = day2 - day1
    in if result < 0 then []
       else if day1 < 32 then 1 :: month_range(day1+1, day2)
       else what_month(day1) :: month_range(day1+1, day2)
    end

fun oldest (dates : (int*int*int) list) =
    if null dates
    then NONE
    else
	let val result = oldest(tl dates)
	in if isSome result andalso is_older(valOf result, hd dates)
	   then result
	   else SOME (hd dates)
	end
		      
		     
		 		    

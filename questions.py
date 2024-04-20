'''
-- Solve the below SQL problems using the Famous Paintings & Museum dataset:

1) Fetch all the paintings which are not displayed on any museums?
SELECT * FROM public.work
where museum_id is null;

2) Are there museuems without any paintings?
SELECT distinct museum_id FROM public.work
where museum_id is not null;

3) How many paintings have an asking price of more than their regular price? 
select * from product_size
where sale_price > regular_price;

4) Identify the paintings whose asking price is less than 50% of its regular price
select *,sale_price - regular_price as diff from product_size
where sale_price < (regular_price*0.5);

5) Which canva size costs the most?
1. select * 
from canvas_size cs left join product_size ps on cs.size_id::text= ps.size_id
order by ps.sale_price desc limit 1;

2. Using Rank
select cs.label as canva, ps.*
from (select *
        , rank() over(order by sale_price desc) as rnk 
        from product_size) ps
join canvas_size cs on cs.size_id::text=ps.size_id
where ps.rnk=1;

6) Delete duplicate records from work, product_size, subject and image_link tables
delete from work 
	where ctid not in (select min(ctid)
						from work
						group by work_id );

delete from product_size 
where ctid not in (select min(ctid)
                    from product_size
                    group by work_id, size_id );

delete from subject 
where ctid not in (select min(ctid)
                    from subject
                    group by work_id, subject );

delete from image_link 
where ctid not in (select min(ctid)
                    from image_link
                    group by work_id );

7) Identify the museums with invalid city information in the given dataset
select * from museum 
where city ~ '^[0-9]'

8) Museum_Hours table has 1 invalid entry. Identify it and remove it.
delete from museum_hours 
	where ctid not in (select min(ctid)
						from museum_hours
						group by museum_id, day );

9) Fetch the top 10 most famous painting subject
Approach 1:
select count(subject) as subject_count from subject
group by subject order by subject_count desc limit 10;

Approach 2:
select * 
	from (
		select s.subject,count(1) as no_of_paintings
		,rank() over(order by count(1) desc) as ranking
		from work w
		join subject s on s.work_id=w.work_id
		group by s.subject ) x
	where ranking <= 10;

10) Identify the museums which are open on both Sunday and Monday. Display museum name, city.
Approach 1:
select m.name as museum_name,m.city, m.state,m.country
from museum_hours mh 
join museum m on m.museum_id=mh.museum_id
where day='Sunday'
Intersect
select m.name as museum_name,m.city, m.state,m.country
from museum_hours mh 
join museum m on m.museum_id=mh.museum_id
where day='Monday';
Approach 2:
select distinct m.name as museum_name, m.city, m.state,m.country
	from museum_hours mh 
	join museum m on m.museum_id=mh.museum_id
	where day='Sunday'
	and exists (select 1 from museum_hours mh2 
				where mh2.museum_id=mh.museum_id 
			    and mh2.day='Monday');

11) How many museums are open every single day?


12) Which are the top 5 most popular museum? (Popularity is defined based on most no of paintings in a museum)

13) Who are the top 5 most popular artist? (Popularity is defined based on most no of paintings done by an artist)

14) Display the 3 least popular canva sizes

15) Which museum is open for the longest during a day. Dispay museum name, state and hours open and which day?

16) Which museum has the most no of most popular painting style?

17) Identify the artists whose paintings are displayed in multiple countries

18) Display the country and the city with most no of museums. Output 2 seperate columns to mention the city and country. If there are multiple value, seperate them with comma.

19) Identify the artist and the museum where the most expensive and least expensive painting is placed. Display the artist name, sale_price, painting name, museum name, museum city and canvas label

20) Which country has the 5th highest no of paintings?

21) Which are the 3 most popular and 3 least popular painting styles?

22) Which artist has the most no of Portraits paintings outside USA?. Display artist name, no of paintings and the artist nationality.

'''
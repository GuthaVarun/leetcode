# Write your MySQL query statement below
select P.firstName, P.lastName, a.city ,a.state  from Person p  left join Address a 
on p.personId = a.personId
import calendar
# for i in range(1,13):
#     print(calendar.month(2022,i),end=" ")
# print(calendar.leapdays(2002 , 2024)) it will print number of leap year b/w given years
k=calendar.monthcalendar(2001,6)
for i in k:
    print(*i)
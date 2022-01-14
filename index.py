#在Python3上工作

import random

when = ["Last year", "Last century", "Last week"]
who = ["Stalin was", "Lening was", "Hitler was"]
where = ["in Moscow", "in Stalingrad"]
did = ["fucking", "playing with"]
what = ["98K", "T-34"]

when_ = when[random.randint(0, len(when)-1)]
who_ = who[random.randint(0, len(who)-1)]
where_ = where[random.randint(0, len(where)-1)]
did_ = did[random.randint(0, len(did)-1)]
what_ = what[random.randint(0, len(what)-1)]

print(when_+","+who_+" "+did_+" "+what_+" "+where_)

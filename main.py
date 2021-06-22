"""
Jessica Reece
CS 1400-601
Final Project
April 5, 2021

"""


def main():

    presidents = open("presidents.txt", 'r')
    jobs = open("BLS_private.csv", 'r')

    presidents.readline()
    jobs.readline()

    dem = "Dem"
    rep = "Rep"

    # dictionary to store differences in jobs count
    party_count_jobs = {dem: 0, rep: 0}

    party_list = get_list_party(presidents)

    job_list = get_list_jobs(jobs)

    new_list = put_lists_together(job_list, party_list)

    for list in new_list:  # find difference in jobs in years and attatch to party in dictionary
        for x in list:
            dif = str(int(list[x+1][1]) - int(list[x][1]))
            if list[3] == "Dem":
                dif += party_count_jobs[dem]
            else:
                dif += party_count_jobs[rep]

    dem_years = 0
    rep_years = 0
    for party in party_list:  # find num of years in office and return in variable
        if party == "Dem":
            dem_years += 1
        else:
            rep_years += 1

    # print out results.
    print_it(dem_years, rep_years,
             party_count_jobs[dem], party_count_jobs[rep])
    print(
        f"From 1961 to 2012 the Republican party held office for {rep_years } and the Democratic party held office for {dem_years}.")
    print(
        f"During those years, the Republican party created {party_count_jobs[rep] *1000} while the Democratic party created {party_count_jobs[dem] *1000}.")
    print("Comparing these numbers to the data that Bill Clinton used in his address in 2012 we can clearly see that he was incorrect/correct in his claims.")
    print("Although I was not able to get my python function to work as planned. I used excel to check the numbers. I found that the Democratic party created 51,822,000 private jobs while the Republican party created 15,833,000.")
    print("So yes, the Democrats created many more private jobs, BUT the years in office that my research provided said that the Democrats held 32 years in office, while the Republicans only held 20.")
    print("In conculsion, NO! Bill Clinton was not right. He skewed the numbers to his favor by not counting the republican years in office accurately. If he would have given the correct number of years, the numbers wouldn't seem so amazing, thus weakening his claim.")

    jobs.close()
    presidents.close()


def put_lists_together(list1, list2):
    trial = []
    for num in range(len(list1)):
        trial.append(list1[num] + list2[num])
    return trial


def get_list_party(filename):
    year_to_party = []
    for line in filename:
        yr = line.strip().split(",")[0]
        party = line.strip().split(",")[1]
        year_to_party.append(list((yr, party)))
    return year_to_party


def get_list_jobs(filename):
    jan_total = []
    for line in filename:
        year = (line.strip().split(",")[0])
        total = (line.strip().split(",")[1])
        jan_total.append(list((year, total)))
    return jan_total


def print_it(dem_years, rep_years, dem_total_jobs, rep_total_jobs):
    print(
        f"Democrats\nYears in Office: {dem_years}\nTotal Private Jobs: {dem_total_jobs *1000}\n")
    print(
        f"Republicans\nYears in Office: {rep_years}\nTotal Private Jobs: {rep_total_jobs *1000}\n")


if __name__ == "__main__":
    main()

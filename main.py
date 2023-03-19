def parallel_processing(n, m, data):
    output = []
    thread_times =[0]*n

    for i in range(m):
        min_time = min(thread_times)
        thread_index = thread_times.index(min_time)

        output.append((thread_index, min_time))
        if i<len(data):
            thread_times[thread_index]+=data[i]
    return output
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m =map(int,input().split())
    data = list(map(int,input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, start_time in result:
        print(thread_index, start_time)



if __name__ == "__main__":
    main()

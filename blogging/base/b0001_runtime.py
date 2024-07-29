import time

if __name__ == "__main__":
    start_time = time.time()

    # Main Program Code
    time.sleep(1)

    # runtime print
    print(f"""Run Time {(time.time() - start_time)} seconds""")
    print("Run Time %s seconds" % (time.time() - start_time))

    # or decimal point control
    print(f"""Run Time {round((time.time() - start_time),2)} seconds""")
    print("Run Time %.2f seconds" % (time.time() - start_time))
    print("Run Time {:.2f} seconds".format(time.time() - start_time))
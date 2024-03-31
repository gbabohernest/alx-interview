# 0x03. Log Parsing
`Algorithm` `Python`


This Python script reads log entries from stdin, computes metrics, and prints statistics based on the input data. The input log entries are expected to follow a specific format:

`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

If a line in the input does not match this format, it is skipped.

### Algorithm

1. Initialize a dictionary `status_code_counts` to keep track of the counts of different `status codes (200, 301, 400, 401, 403, 404, 405, 500)`.

2. Initialize variables `lines_processed` and `size` to keep track of the number of lines processed and the total file size, respectively.

3. Read input lines from stdin.

4. For each line:
    - Split the line into parts using whitespace as the delimiter.
    -  If the line does not have at least 7 parts (meaning it does not match the expected format), skip to the next line.
    - Increment the `lines_processed` count.
    - Add the file size (last part of the line) to the `size`.
    - Extract the status code (second-to-last part of the line) and update the corresponding count in `status_code_counts`.
    - If lines_processed is a multiple of 10, print the current statistics.

5. If a keyboard interrupt (CTRL + C) occurs, print the final statistics and raise the interrupt.

6. Print the final statistics after processing all input lines.

#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("testing.txt", "w+")


  # Open the file for appending text to the end
  f = open("testing.txt", "r")

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is a line " + str(i) + "\r\n")
  #
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode == "r":
    # contents = f.read()
    # print(contents)
    fl = f.readlines()
    for x in fl:
      print(x)

    
if __name__ == "__main__":
  main()

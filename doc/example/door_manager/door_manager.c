#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int setPin(unsigned char pin, bool value)
{
  FILE * pinf = 0;
  char buffer[64];
  snprintf(buffer, 64, "/sys/class/gpio/gpio%d/value", pin);

  // open pgio device
  pinf = fopen(buffer, "w");
  if (pinf) {
    int result;
    if (value) {
      result = fwrite("1", 1, 1, pinf);
      //printf("on%d",pin);
    } else {
      result = fwrite("0", 1, 1, pinf);
      //printf("off%d",pin);
    }
    
    fclose(pinf);
    // return result of the operation (result is 1 if things went ok)
    return ! result;
  } else {
    // error opening file
    return 1;
  }
}

int openDoor()
{
  int result;
  printf("Opening door.. ");
  result = setPin(24, true);
  result = setPin(24, false);
  printf("%s\n", result ? "failed!" : "complete!");
  return result;
}

int closeDoor()
{
  int result;
  printf("Closing door.. ");
  result = setPin(23, true);
  result = setPin(23, false);
  printf("%s\n", result ? "failed!" : "complete!");
  return result;
}


void displayUsage(const char * progname)
{
  printf("Usage: %s OPTION\n", progname);
}

void displayLongHelp(const char * progname)
{
  displayUsage(progname);
  printf("\nAvailable OPTIONs are:\n"
	 "  -h, --help   Display this help.\n"
	 "  -o, --open   Open the door.\n"
	 "  -c, --close  Close the door.\n\n"
	 "Returns: 0 on success, 1 otherwise.\n");
}


int main(int argc, const char ** argv, const char ** envp)
{
  if (argc == 2) {
    const char * param = argv[1];

    // process all known parameter values
    if ((strcmp("-o", param) && strcmp("--open", param)) == 0) {
      return openDoor();
    } else if ((strcmp("-c", param) && strcmp("--close", param)) == 0) {
      return closeDoor();
    } else if ((strcmp("-h", param) && strcmp("--help", param)) == 0) {
      displayLongHelp(argv[0]);
      return 0;
    }
  }

  printf("Invalid or no parameters given!\n\n");
  displayLongHelp(argv[0]);
  return 1;
}

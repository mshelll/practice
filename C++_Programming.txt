// Coding problem: 45 minute time limit.

// PROBLEM DEFINITION
// ------------------
// Reverse each word in the input string.
// The order of the words will be unchanged.
// A word is made up of letters and/or numbers.
// Other characters (spaces, punctuation) will not be reversed.

// NOTES
// ------
// Write production quality code
// We prefer clarity over performance (though if you can achieve both - great!)
// You can use the language that best highlights your programming ability
//    the template below is Python – but you can write
//    in Java/C++/C#/Haskell/etc if you feel you solve the
//    problem better in that language.
// A working solution is preferred (assert in main() should succeed)
// Bonus points for good tests

#include <string>
#include <assert.h>
#include <ctype.h>
#include <unordered_map>
#include <map>


/*
  Reverse a substring in str from start to end
*/
void reverse(std::string& str, int start, int end)
{
  int mid = (int)(end-start)/2;

  for(int i = 0; i <= mid; i++)
  {
    char t = str[start+i];
    str[start+i] = str[end-i];
    str[end-i] = t;
  }
}

/*
  Iterate through the sentence find start and end index of word
  invoke routine for reversing the word. continue to find next word

  Time complexity : O(n)
  Space complexity : O(1)
*/
std::string reverse_words(const std::string &str)
{

    std::string temp(str);

    int start = -1, end = -1;

    bool wordstart = false;

    for(int i=0; i<=temp.size(); i++)
    {
      if (isalnum(temp[i]) && !wordstart)
      {
        start = i;
        wordstart = true;
      }
      else if( ( !isalnum(temp[i]) || i==temp.size() ) && wordstart)
      {
        end = i-1;
        wordstart = false;
        reverse(temp, start, end);
      }
    }

    return temp;
}

int main()
{

    std::unordered_map<std::string, std::string> test_cases;

    test_cases["String;   2be reversed..."] = "gnirtS;   eb2 desrever...";
    test_cases["String;   2be reversed"] = "gnirtS;   eb2 desrever";
    test_cases[";;String;   2be reversed..."] = ";;gnirtS;   eb2 desrever...";
    test_cases[";;String;   2be reversed"] = ";;gnirtS;   eb2 desrever";
    test_cases[";;String;   2be reversed..."] = ";;gnirtS;   eb2 desrever...";
    test_cases["String;   2be reve;rsed..."] = "gnirtS;   eb2 ever;desr...";
    test_cases["This is a sentence."] = "sihT si a ecnetnes.";
    test_cases["  This is a sentence."] = "  sihT si a ecnetnes.";
    test_cases["This is a sentence.  "] = "sihT si a ecnetnes.  ";
    test_cases["This is a sentence.  "] = "sihT si a ecnetnes.  ";
    test_cases["madam is a palindrome.  "] = "madam si a emordnilap.  ";
    test_cases["madam radar level kayak.  "] = "madam radar level kayak.  ";
    test_cases["Aa Bb Dear"] = "aA bB raeD";
    test_cases["S# ^& Dear"] = "S# ^& raeD";
    test_cases["123 456 78"] = "321 654 87";
    test_cases["gnirtS;   eb2 desrever..."] = "String;   2be reversed...";
    test_cases[""] = "";

    std::unordered_map<std::string, std::string>::iterator itr;
    int count = 0;
    for(itr=test_cases.begin(); itr != test_cases.end(); itr++)
    {
      printf("\n\n Test No : %d", count++);
      printf("\n input : %s", itr->first.c_str());
      printf("\n expected : %s", itr->second.c_str());
      fflush(stdout);
      assert(reverse_words(itr->first) == itr->second);
    }

    return 0;
}
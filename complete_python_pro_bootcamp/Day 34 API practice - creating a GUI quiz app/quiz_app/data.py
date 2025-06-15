import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print('💽 QUESTION DATA', question_data)


# question_data = [
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "The logo for Snapchat is a Bell.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "A Mac is not a PC",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "A Boolean value of &quot;0&quot; represents which of these words?",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "hard",
#     "category": "Science: Computers",
#     "question": "DHCP stands for Dynamic Host Configuration Port.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "The Windows ME operating system was released in the year 2000.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The &#039;Raspberry Pi&#039; series of single-board computers were created in the United States.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "MacOS is based on Linux.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "Ada Lovelace is often considered the first computer programmer.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "AMD created the first consumer 64-bit processor.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The HTML5 standard was published in 2014.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "hard",
#     "category": "Science: Computers",
#     "question": "The T-Mobile Sidekick smartphone is a re-branded version of the Danger Hiptop.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "It&#039;s not possible to format a write-protected DVD-R Hard Disk.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "Android versions are named in alphabetical order.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "hard",
#     "category": "Science: Computers",
#     "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The open source program Redis is a relational database server.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "Time on Computers is measured via the EPOX System.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The common software-programming acronym &quot;I18N&quot; comes from the term &quot;Interlocalization&quot;.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The first computer bug was formed by faulty wires.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "RAM stands for Random Access Memory.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "The first IBM PC was released in 1981.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "Linux was first created as an alternative to Windows XP.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "medium",
#     "category": "Science: Computers",
#     "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
#     "correct_answer": "True",
#     "incorrect_answers": [
#       "False"
#     ]
#   },
#   {
#     "type": "boolean",
#     "difficulty": "easy",
#     "category": "Science: Computers",
#     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#     "correct_answer": "False",
#     "incorrect_answers": [
#       "True"
#     ]
#   }
# ]

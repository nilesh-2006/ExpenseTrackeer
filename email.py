email = input("Enter your Email: ")

# flags
space_found = False
uppercase_found = False
invalid_char_found = False

# ---------- RULE 1: Minimum Length ----------
if len(email) < 6:
    print("❌ Invalid Email: Minimum length must be at least 6 characters.")
    exit()

# ---------- RULE 2: Must start with a letter ----------
if not email[0].isalpha():
    print("❌ Invalid Email: It must start with an alphabet (a-z).")
    exit()

# ---------- RULE 3: Must contain exactly one '@' ----------
if ("@" not in email) or (email.count("@") != 1):
    print("❌ Invalid Email: Email must contain exactly one '@'.")
    exit()

# ---------- RULE 4: Dot must be at -3 OR -4 position ----------
if len(email) < 4 or not (email[-4] == "." or email[-3] == "."):
    print("❌ Invalid Email: Dot (.) must be 3rd or 4th position from the end.")
    exit()

# ---------- RULE 5: Character-by-character checks ----------
for ch in email:
    if ch.isspace():
        space_found = True
    elif ch.isupper():
        uppercase_found = True
    elif ch.isdigit():
        continue
    elif ch.isalpha():
        continue
    elif ch in ("_", ".", "@"):
        continue
    else:
        invalid_char_found = True

# ---------- RULE 6: Flag Checks ----------
if space_found:
    print("❌ Invalid Email: Email must not contain spaces.")
    exit()

if uppercase_found:
    print("❌ Invalid Email: Uppercase letters are not allowed.")
    exit()

if invalid_char_found:
    print("❌ Invalid Email: Contains invalid special characters.")
    exit()

# ---------- If everything is correct ----------
print("✅ Valid Email!")

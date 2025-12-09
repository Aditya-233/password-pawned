# Password Pwned Checker

This script checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP) Pwned Passwords API**. It uses a privacy‑preserving technique (k‑anonymity) by only sending the first 5 characters of the password’s SHA‑1 hash to the API.

---

## Features

* No plaintext passwords are ever sent over the network
* Uses SHA‑1 hashing with the HIBP range API
* Simple CLI usage
* Returns how many times a password was found in breaches

---

## Requirements

* Python 3.7+
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## Usage

Run the script with one or more passwords as arguments:

```bash
python3 checker.py qwerty abcd abc1234
```

Output example:

```
qwerty is pawned 123456 times
abcd is pawned 0 times
abc1234 is pawned 532 times
```

If the count is `0`, the password was not found in the dataset.

---

## How It Works

1. The password is hashed using SHA‑1.
2. The first 5 characters of the hash are sent to the HIBP API.
3. The API returns a list of hash suffixes and breach counts.
4. The script checks if the remaining part of your hash exists in the response.
5. If found, it prints how many times it appeared in breaches.

---

## Limitations

* Depends on internet connection
* API rate limits apply
* Not suitable for bulk scanning at high volume without optimization

---

## Performance Notes

You can improve speed for large password lists by:

* Adding threading or async requests
* Avoiding dictionary creation by checking the hash tail directly during iteration

---

## Security Notice

This tool is for educational or defensive use only. Never use it to test passwords you do not own or have permission to assess.

---

## License

MIT License

---

## Author

Built for fast and private password breach checks using public security APIs.

# Labs

These are labs for those who are learning how to develop secure software.
See our [introduction](introduction) for more information.
They're designed to support our free course
[Developing Secure Software (LFD121)](https://training.linuxfoundation.org/training/developing-secure-software-lfd121/).

You can download the labs in these sections, e.g., to run locally
without Internet access. Labs with a locale prefix are for that locale (e.g., [ja_hello](ja_hello.html) is the Japanese translation of [hello](hello.html)).

We *want* people to create more labs! Here's more information about
how to do that and the labs we'd like created.

## Sample available labs

Here are some of the labs available, which you can use as examples:

* [hello](hello.html) - simple "Hello, world!" demo. ([ja_hello](ja_hello.html), [fr_hello](fr_hello.html))
* [input1](input1.html) - input validation (simple types) ([ja_input1](ja_input1.html))
* [regex0](regex0.html) - regular expressions (regexes) - introduction ([ja_regex0](ja_regex0.html))
* [regex1](regex1.html) - regular expressions (regexes)  ([ja_regex1](ja_regex1.html))
* [input2](input2.html) - input validation (more complex situations) ([ja_input2](ja_input2.html))
* [csp1](csp1.html) - Content Security Policy (CSP) ([ja_csp1](ja_csp1.html))
* [oob1](oob1.html) - Out-of-bounds (OOB) ([ja_oob1](ja_oob1.html))
* [handling-errors](handling-errors.html) - Handling errors ([ja_handling-errors](ja_handling-errors.html))

We also have a [template](template.html) available.

## Please contribute labs

Please help us create labs! See "[Please help us create labs!](https://docs.google.com/document/d/1wNoNjLpdkgoXkRDvDBI32tm62rbASlfF6gxwyEkyTYs/edit)" for why it's
important to help us create labs.

We would love to have people contribute relevant labs to help
people learn how to develop secure software.
We'd be happy to give you credit through a "wall of fame".

If you're interested, please contact
[David A. Wheeler](mailto:dwheele&#114;&#64;linuxfoundation&#46;org).
See below for how to create labs and our lab roadmap.

## Please help us translate labs

We'd love to have labs available in various natural languages!
You can take existing labs and translate them. For technical details, see the
[information on lab localization](create_checker#localization).
Let us know if you're doing it!
Please see [how to contribute labs](#please-contribute-labs) for more.

## How to create and submit labs

See [create labs](create_labs) if you want to learn how to create labs.
In particular, that page will link to how to
[create labs using checker](create_checker).
We suggest using the [template](template.html) as a start.

To submit new or updated labs, create a pull request on the
[OpenSSF Best Practices Working Group (WG) repository](https://github.com/ossf/wg-best-practices-os-developers/)
under the `docs/labs` directory.
Simply fork the repository, add your proposed lab in the `docs/labs` directory,
and create a pull request.

## Lab Roadmap

We plan to create labs for the secure software development
fundamentals course;
[here is its development website](https://github.com/ossf/secure-sw-dev-fundamentals).

Below are the sections where we plan to create labs, along with
mappings to existing labs or people who have agreed to work on one.
The items marked "PLANNED" with "-1" are those we intend to do first;
"PLANNED" with "-2" are planned in a second pass, "PLANNED" with "-0"
were done early.
The term "PLANNED" is replaced with "DONE" as they're done.
The ones marked "UNASSIGNED" are ones where no one has (yet) agreed to
work on.

* Input Validation
  * Input Validation Basics
    * [Input Validation Basics Introduction](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#input-validation-basics-introduction) - DONE-0 [hello](hello.html) [ja_hello](ja_hello.html)
    * [How Do You Validate Input?](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#how-do-you-validate-input), [Input Validation: Numbers and Text](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#input-validation-numbers-and-text)
  * Input Validation: Numbers and Text
    * Input Validation: A Few Simple Data Types - DONE-0 [input1](input1.html)
    * [Sidequest: Text, Unicode, and Locales](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#sidequest-text-unicode-and-locales)
    * [Validating Text](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#validating-text)
    * Introduction to Regular Expressions - DONE-0 [regex0](regex0.html)
    * Using Regular Expressions for Text Input Validation - DONE-0 [regex1](regex1.html), [input2](input2.html)
    * [Countering ReDoS Attacks on Regular Expressions](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#countering-redos-attacks-on-regular-expressions) - DONE-2 (Camila Vilarinho, 2026-07-19) [redos](redos.html)
  * Input Validation: Beyond Numbers and Text
    * [Insecure Deserialization](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#insecure-deserialization) - PLANNED-2 (Camila Vilarinho) [deserialization](deserialization.html)
    * [Input Validation: Beyond Numbers and Text](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#input-validation-beyond-numbers-and-text) - PLANNED-2 UNASSIGNED
    * [Minimizing Attack Surface, Identification, Authentication, and Authorization](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#minimizing-attack-surface-identification-authentication-and-authorization) - PLANNED-2 UNASSIGNED
    * [Search Paths and Environment Variables (including setuid/setgid Programs)](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#search-paths-and-environment-variables-including-setuidsetgid-programs) - PLANNED-2 UNASSIGNED
    * [Special Inputs: Secure Defaults and Secure Startup](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#special-inputs-secure-defaults-and-secure-startup) - PLANNED-2 UNASSIGNED
  * Consider Availability on All Inputs
    * [Consider Availability on All Inputs Introduction](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#consider-availability-on-all-inputs-introduction) - PLANNED-2 UNASSIGNED
* Processing Data Securely
  * Processing Data Securely: General Issues
    * [Prefer Trusted Data. Treat Untrusted Data as Dangerous](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#prefer-trusted-data-treat-untrusted-data-as-dangerous) - PLANNED-2 UNASSIGNED
    * [Avoid Default & Hardcoded Credentials](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#avoid-default--hardcoded-credentials) - DONE-1 (David A. Wheeler) [hardcoded](./hardcoded.html)
    * [Avoid Incorrect Conversion or Cast](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#avoid-incorrect-conversion-or-cast) - DONE-2 (Keith Grant via Vincent Danen, by 2024-07-26) [conversion](conversion.html)
  * Processing Data Securely: Undefined Behavior / Memory Safety
    * Countering Out-of-Bounds Reads and Writes (Buffer Overflow) - DONE-0 [oob1](oob1.html)
    * [Double-free, Use-after-free, and Missing Release](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#double-free-use-after-free-and-missing-release) <!-- was Bennett Pursell --> - DONE-1 (David A. Wheeler) [free](free.html)
    * [Avoid Undefined Behavior](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#avoid-undefined-behavior) - PLANNED-2 UNASSIGNED
  * Processing Data Securely: Calculate Correctly
    * [Avoid Integer Overflow, Wraparound, and Underflow](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#avoid-integer-overflow-wraparound-and-underflow) - PLANNED-2, first draft by 2024-07-19 (Petr Matousek via Vincent Danen)
* Calling Other Programs
  * Introduction to Securely Calling Programs
    * Introduction to Securely Calling Programs - The Basics
  * Calling Other Programs: Injection and Filenames
    * [SQL Injection](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#sql-injection) - DONE-1 (@Elijah Everett, 2024-08-13) [sql-injection](sql-injection.html)
    * OS Command (Shell) injection - DONE-1 (Marta Rybczynska) [shell-injection](shell-injection.html) [argument-injection](argument-injection.html)
    * [Other Injection Attacks](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#other-injection-attacks) - PLANNED-2 (Dhananjay Arunesh via Vincent Danen, 2026-07-26)
    * Filenames (Including Path Traversal and Link Following) - PLANNED-2 UNASSIGNED
  * Calling Other Programs: Other Issues
    * [Call APIs for Programs and Check What Is Returned](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#call-apis-for-programs-and-check-what-is-returned) - PLANNED-2 UNASSIGNED
    * [Handling Errors](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#handling-errors) - DONE-2 (Avishay Balter) [handling-errors](handling-errors.html)
    * [Logging](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#logging) - PLANNED-2 UNASSIGNED
    * [Debug and Assertion Code](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#debug-and-assertion-code) - DONE-1 (David A. Wheeler) <!-- was: Jason Shepherd --> [assert](assert.html)
    * Countering Denial-of-Service (DoS) Attacks - PLANNED-2 UNASSIGNED
* Sending Output
  * [Introduction to Sending Output](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#introduction-to-sending-output) - PLANNED-2 UNASSIGNED
  * [Countering Cross-Site Scripting (XSS)](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#countering-cross-site-scripting-xss) - DONE-1 (David A. Wheeler) [xss](xss.html)
  * Content Security Policy (CSP) - DONE-0 [csp1](csp1.html)
  * Other HTTP Hardening Headers - (probably continue csp1) PLANNED-2 UNASSIGNED
  * [Cookies Cookies & Login Sessions Login Sessions](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#cookies--login-sessions) - PLANNED-2 (Dhananjay Arunesh via Vincent Danen)
  * [CSRF / XSRF](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#csrf--xsrf) - PLANNED-2 UNASSIGNED
  * [Open Redirects and Forwards](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#open-redirects-and-forwards) - PLANNED-2 UNASSIGNED
  * HTML **target** and JavaScript **window.open()** - PLANNED-2 UNASSIGNED
  * Using Inadequately Checked URLs / Server-Side Request Forgery (SSRF) - PLANNED-2 UNASSIGNED
  * Same-Origin Policy and Cross-Origin Resource Sharing (CORS) - PLANNED-2 UNASSIGNED
  * [Format Strings and Templates](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#format-strings-and-templates) - DONE-1 (Jason Shepherd) [format-strings](https://best.openssf.org/labs/format-strings.html)
  * [Minimize Feedback / Information Exposure](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#minimize-feedback--information-exposure) - PLANNED-2 (Ibrahim Mukherjee, 2026-08-07)
  * [Avoid caching sensitive information](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#avoid-caching-sensitive-information) - PLANNED-2 UNASSIGNED
  * [Side-Channel Attacks](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md#side-channel-attacks) - PLANNED-2 UNASSIGNED

## Our thanks

Thanks to the following people who have created or offered to create labs
(sorted by given/first name):

* Avishay Balter (Microsoft)
* Camila Vilarinho
* David A. Wheeler (Linux Foundation)
* Dhananjay Arunesh
* Elijah Everett
* Emily Lovell
* Jason Shepherd
* Jeremiah Howard
* Keith Grant
* Liran Tal
* Marta Rybczynska
* Petr Matousek
* Tapas Jena

## Other information

You can find the current version of this page at the
[OpenSSF Best Practices WG labs](https://best.openssf.org/labs/) site.

All code to implement the labs is released under the MIT license.
All text is released under the Creative Commons Attribution (CC-BY-4.0)
license.

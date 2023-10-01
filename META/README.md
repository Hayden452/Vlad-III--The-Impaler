Vlad 1.0:
=============================
Takes a Google Form, seeks out areas for user input, determines what is being 
asked of the user, then chooses fake information to fill in. 

Vlad 1.1:
=============================
Final version unless I get bored. 

Requires manual loading of the Google Form to poison. Will not take any other 
kind of form, only Google forms. Limited knowledge of phishing terms, will only 
detect blatant PII phishing.

=====================================================================================================
=====================================================================================================

Suggestions for Use:
=============================
* This tool is most useful when attacking phishing forms that do not require a sign-in, for 3 reasons:
    1) Having to sign in to an account (to get into a form) repeatedly might alert Google or Microsoft, and 
       very little can be done to prevent this.
    2) In some cases, only one response is allowed per person. 
    3) Phishers will be able to differentiate real from fake responses if the account creating the responses is linked to the response. 
   It may be beneficial to use a different method of retaliation if a form requires sign-in.

* Keep previously attacked phishing spots in the database for the off-chance that a form is re-used. If it is not re-used, no harm done. 

* If possible, keep this tool running on a dedicated machine, as more submitted fake forms makes it harder to distinguish legitimate forms. 

* Seek out phishing forms to punish, but ensure that Vlad's target is a legitimate threat. 
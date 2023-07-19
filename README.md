## myvinted

Just having fun trying to get some data from the Vinted api and building a nice and hopefully clean python project :)

What I learned so far:
- to actually be able to call the vinted api, you need to set a cookie in the header that contains a real value for `_vinted_fr_session=`
- so you first have to get that cookie,
- and then put that cookie in the headers when you do an actual call to the vinted api, for example: https://www.vinted.nl/api/v2/languages
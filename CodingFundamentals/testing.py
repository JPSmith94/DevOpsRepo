#testing

#we can potentially have lots errors in our code, so we need to test it 
#write tests is cheaper than refactoring code after deployment
#even if we are only doing a canary deployment if we haven't tested we have to spend a lot of time/money to fix found issues
#types of tests: unit tests - tests each block of code/function in isolation
#               intergration testing - how does the code work in relation to other code
#               user acceptance testing - does the app do what its suppose to do (Jason/Kerry)
#               QA testing - rules + regulations ect... are we breaking the law with our app ect.. is there proper intergrity, is data being handled correctly
#               non - functional testing (monitoring)
#               performance, scalability, usability, up time
#               maintenance testing - we push a change to our code and see what happens (trying to introduce problems)
#
# 

#install pip- 
#install pytest

#if we start the name of our file with test_**.py or ***_test.py if we follow this naming convention we can just run pytest

#pytest this _is_a_testing_file.py < would need to specify
#pytest test_file.py < should be automatic
pip3 --version

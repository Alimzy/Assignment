nokia = """
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. Sim services

"""
print(nokia)

nokia = int(input("Enter an option: "))
        
match nokia:
    case 1:
        phone_book_menu ="""
        1. Search
        2. Service Nos
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. send b'card
        8. Options
        9. Speed dials
        10. Voice tags
        """
        print(phone_book_menu)    
        phone_book = int(input("Enter an option: "))
        match phone_book:
                                                   
            case 1:
                print("Search")
            case 2: 
                print("Service Nos") 
            case 3:
                print("Add name")
            case 4:
                print("Edit")
            case 5:
                print("Edit")
            case 6:
                print("Assign tone")
            case 7:
                print("Send b'card")
            case 8:
                option_menu = """
                 1. Type of view
                 2. Memory status
                """
                print(option_menu)
                options = int(input("Enter an option: "))
                match options:
                    case 1:
                        print("Type of view")
                    case 2:
                        print("Memory status") 
            case 9: 
                print("Speed dials")    
            case 10:
                print("Voice tags")
    case 2: 
        messages_menu = """
         1. Write messages
         2. Inbox
         3. Outbox
         4. Picture messages
         5. Templates
         6. Smileys
         7. Messages settings
         8. info service
         9. Voice mailbox number
        10. Service command editor      
        """
        print(messages_menu)
        messages = int(input("Enter an option: "))
        match messages: 
            
             case 1: 
                 print("Write messages")
             case 2:
                 print("Inbox")
             case 3:
                 print("Outbox")
             case 4:
                 print("Picture messages")
             case 5:
                 print("Templates")
             case 6:
                 print("Smileys")
             case 7:
                message_settings_menu = """
                1. Set 1
                2. Common
                """
                print(message_settings_menu)
                message_setting = int(input("Enter an option: "))
                match message_setting:
                    case 1:
                        set_menu = """
                        1. Message centre number
                        2. Message sent as
                        3. Message validity
                                   """
                        print(set_menu)
                        set_one = int(input("Enter an option: "))  
                        match set_one:
                            case 1:
                                print("Message centre number")
                            case 2:
                                print("Message sent as")
                            case 3:
                                print("Message validity")
                    case 2:
                        common_menu = """
                        1. Delivery reports
                        2. Reply via same centre
                        3. Character support
                        """
                        print(common_menu)
                        common = int(input("Enter an option: "))
                        match common:
                            case 1:
                                print("Delivery reports")
                            case 2:
                                print("Reply via same centre")
                            case 3:
                                print("Character support")
             
             case 8:
                print("Info service")
             case 9: 
                print("Voice mailbox number")
             case 10: 
                print("Service command editor")    
            
    case 3:
        print("Chat")
    case 4:
        call_register_menu = """
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. call cost settings
        8. Prepaid credit
        """
        print(call_register_menu)
        call_register = int(input("Enter an option: "))
        match call_register:
            case 1: 
                print("Missed calls")
            case 2:
                print("Received calls")
            case 3:
                print("Dialled numbers")
            case 4:
                print("Erase recent call lists")
            case 5:
                call_duration_menu = """
                1. Last call duration
                2. All calls' duration
                3. Received call duration
                4. Dialled calls' duration
                5. Clear timers
                """
                print(call_duration_menu)
                call_duration = int(input("Enter an option: "))
                match call_duration:
                    case 1:
                        print("Last call duration")
                    case 2:
                        print("All calls' duration")
                    case 3:
                        print("Received call duration")
                    case 4:
                        print("Dialled calls' duration")
                    case 5:
                        print("Erase recent call lists")
                        
            case 6:
                call_cost_menu = """
                1. Last call costs
                2. All calls' cost
                3. Clear counters
                """
                print(call_cost)
                call_cost = int(input("Enter an option: "))
                match call_cost:
                    case 1:
                        print("Last call costs")
                    case 2:
                        print("All call costs")
                    case 3:
                       print("Clear counters")                   
            case 7:
               call_cost_settings_menu = """
               1. Call cost limit
               2. Show costs in
               """
               print(call_cost_settings_menu)
               call_cost_settings = int(input("Enter an option: "))
               match call_cost_settings:
                    case 1:
                        print("Call cost limit")
                    case 2: 
                        print("Show costs in")
            case 8:
                print("Prepaid credit")
                
    case 5:
        tones_menu = """
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        """
        print(tones_menu)
        tones = int(input("Enter an option: "))
        match tones:
            case 1:
                print("Ringing tone")
            case 2:
                print("Ringing volume")
            case 3:
                print("Incoming call alert")
            case 4:
                print("Composer")
            case 5:
                print("Message alert tone")
            case 6:
                print("Keypad tones") 
            case 7:
                print("Warning and game tones")
            case 8:
                print("Vibrating alert")
            case 9:
                print("Screen saver")
    case 6:
        setting_menu = """
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        """
        print(setting_menu)
        settings = int(input("Enter an option: "))
        match settings:
            case 1:
                call_setting_menu = """
                1.Automatic redial
                2. Speed dialing
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Confirm SIM service actions
                """
                print(call_setting_menu)
                call_setting = int(input("Enter an option: "))
                match call_setting:
                    case 1:
                        print("Automatic redial")
                    case 2:
                        print("Speed dialing")
                    case 3:
                        print("Call waiting options")
                    case 4:
                        print("Own number sending")
                    case 5: 
                        print("Phone line in use")
                    case 6:
                        print("Confirm SIM service actions")
            case 2:
                phone_settings_menu = """
                1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                5. Lights
                6. Confirm SIM service action
                """
                print(phone_settings_menu)
                phone_setting = int(input("Enter an option: "))
                match phone_setting:
                    case 1:
                        print("Language")
                    case 2:
                        print("Cell info display")
                    case 3:
                        print("Welcome note")
                    case 4:
                        print("Network selection")
                    case 5:
                        print("Lights")
                    case 6:
                        print("Confirm Sim service action")
            case 3:
                security_setting_menu ="""
                1. PIN code request
                2. Call baring service
                3. Fixed dialling
                4. Closed user group
                5. Phone security
                6. Change access code
                """
                print(security_setting_menu)
                security_setting = int(input("Enter an option: "))
                match security_setting:
                    case 1: 
                        print("PIN code request")
                    case 2:
                        print("Call baring service")
                    case 3:
                        print("Fixed dialling")
                    case 4:
                        print("Closed user group")
                    case 5:
                        print("Phone security")
                    case 6:
                        print("Change access code")
            
            case 4:
                print("Restore factory settings")
    case 7:
        print("Call divert")
    case 8:
        print("Games")
    case 9:
        print("calculator")
    case 10:
        print("Reminders")
    case 11:
        clock_menu = """
        1. Alarm clock
        2. Clock settings
        3. Date settings
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        """
        print(clock_menu)
        clock = int(input("Enter an option: "))
        match clock:
            case 1:
                print("Alarm clock")
            case 2:
                print("clock settings")
            case 3:
                print("Date settings")
            case 4:
                print("Stopwatch")
            case 5:
                print("Countdowm timer")
            case 6:
                print("Auto update date and time")
    case 12:
        print("Profiles")
    case 13:
        print("Sim services")

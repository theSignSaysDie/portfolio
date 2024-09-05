[
  To the best of my knowledge, this program is my original creation.
  This accepts a single integer N >= 2 and prints out a square box of that size into the terminal.
]



+++++++++++++++++++++++++++++++++++    Initialize '#' at #0
>
++++++++++                             Initialize '\n' at #1
>

,                                      Accept input byte at #2
[>+>>+<<<-]                            Duplicate input byte to #4 and #6
>>>--                                  Decrement #6 by 2



<<                                     Move to #4
[                                      Print out top edge of box
  -<+<<.>>>                              While shifting #4 to #3: output '#' 
]
<<.                                    Output '\n'
>>>>                                   Go to #6
[                                      Duplicate #6 to #5 and #4
  <+<+>>-
]                              
<<                                     Move to #4 (the midbox counter)


[
  <<<.--->>>>                          Output '#' and change #0 to ' '
  [                                    Print ' 's
    ->+<<<<<.>>>>                      Shifting #5 to #6 and outputting ' ' each shift
  ]
  >                                    Move to #6
  [
    -<+>                               Shift #6 to #5
  ]
  <<<<<+++.>.>>                        Change #0 back to '#'; print; resume loop
  -
]

<                                      Move to #3

[                                      Print out bottom edge of box
  -<<.>>
]
-module(generador).
-export([main/0]).

main() ->
  {ok, File} = file:open("Muestras/muestra_erlang_float.txt", [write]),
  rand:seed(exsplus, erlang:monotonic_time()),
  lists:foreach(
    fun(_) ->
      X = rand:uniform(),
      file:write(File, io_lib:format("~f~n", [X])) end,
    lists:seq(1,1000000)
  ),
  file:close(File).

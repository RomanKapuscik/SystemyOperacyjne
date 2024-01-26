On Error Resume Next
Const ADS_SCOPE_SUBTREE = 2 

'Procedura do zmiany ciągów znaków w plikach
' Przykład Call ini ("d:\plik.txt","ServerName=Server1","ServerName=Server2")
Sub ini (sciezka,nazwa_stara,nazwa_nowa)
  Set objFSO = CreateObject("Scripting.FileSystemObject")
  Set objFile = objFSO.OpenTextFile(sciezka, 1)

  strText = objFile.ReadAll
  objFile.Close
  strNewText = Replace(strText, nazwa_stara, nazwa_nowa,1,-1,1)

  Set objFile = objFSO.OpenTextFile(sciezka, 2)
  objFile.WriteLine strNewText
  objFile.Close
end Sub

'wywołanie funkcji z parametrami
Call ini ("C:\Users\roman\OneDrive\Dokumenty\Semestr_III\Systemy operacyjne\plik.txt","ServerName=Server2","ServerName=Server77")
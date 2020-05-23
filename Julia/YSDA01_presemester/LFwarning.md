* git에서 .jpynb 문서 파일을 add 할 때 이런 에러가 뜬다.
> warning: LF will be replaced by CRLF in ~~~/~~~.ipynb.
> The file will have its original line endings in your working directory.

&nbsp;&nbsp;

> Unix운영체제 에서는 파일의 끝을 LF로 대체하고 windows 운영체제에서는 CRLF로 대체하는데, 큰 문제는 없다는 것 같다.
> * 출처: https://paphopu.tistory.com/entry/git-bash-LF-will-be-replaced-by-CRLF-문제-발생

&nbsp;&nbsp;

> "git config --global core.autocrlf false" 라고 입력해주면 에러가 해결되는 것 같다는데, 그냥 경고를 무시하고 안해줬다.
> * 출처: https://bnzn2426.tistory.com/33

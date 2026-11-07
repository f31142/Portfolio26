# Portfolio26

Jeon의 한국어 포트폴리오입니다. 소개 페이지에는 관심 분야와 학습 목표를, 활동 페이지에는 중앙해커톤에서 진행한 MyLab 프로젝트와 제가 맡은 작업을 정리했습니다. [공개 사이트](https://f31142.github.io/Portfolio26/)

## 로컬 빌드

GitHub Actions와 같은 버전을 사용하려면 아래 도구를 운영체제에 맞게 설치하고, 터미널에서 실행할 수 있도록 PATH에 추가합니다.

- [Python 3.12](https://www.python.org/downloads/)
- [Node.js 24와 npm](https://nodejs.org/en/download)
- [Go 1.27.1](https://go.dev/dl/)
- [Hugo Extended 0.167.0](https://github.com/gohugoio/hugo/releases/tag/v0.167.0)
- [Dart Sass 1.105.0](https://github.com/sass/dart-sass/releases/tag/1.105.0)

`README.md`와 `.github` 폴더가 있는 저장소 루트에서 아래 명령을 순서대로 실행합니다.

```bash
python .github/pages_build.py --dependencies
python .github/pages_build.py --build
```

빌드가 성공하면 저장소 루트의 `public/`에 결과물이 생성됩니다. 홈 페이지 파일은 `public/index.html`입니다.

## 수정과 재배포

| 수정 대상 | 파일 |
| --- | --- |
| 홈 소개, 메뉴, GitHub 링크 | `site/hugo.toml` |
| 소개 본문 | `site/content/about.ko.md` |
| 활동 목록 제목 | `site/content/projects/_index.ko.md` |
| 개별 활동 본문 | `site/content/projects/` 안의 각 `.ko.md` 파일 |
| 자동 배포 설정 | `.github/workflows/hugo-pages.yml` |

수정한 파일을 커밋하고 `main`에 푸시하면 GitHub Actions가 자동 실행됩니다. [Actions](https://github.com/f31142/Portfolio26/actions)에서 해당 커밋의 `build`와 `deploy`가 성공했는지 확인한 뒤, [공개 사이트](https://f31142.github.io/Portfolio26/)에서 변경 내용을 확인합니다.

### 새 활동 추가

1. `site/content/projects/`에 활동마다 새 파일을 만듭니다. 예를 들어 `web-study.ko.md`를 만들면 상세 주소는 `/Portfolio26/projects/web-study/`가 됩니다.
2. 파일 맨 위의 두 `+++` 사이에 `title = "활동 제목"`을 적고, 그 아래에 본문을 작성합니다. 제목은 **Activities** 목록에 자동으로 표시됩니다.
3. 배포 후 목록에서 새 제목을 눌러 상세 페이지가 열리는지 확인합니다.

## 출처와 이용 조건

- 테마는 Luiz F. A. de Prá와 기여자가 만든 [Hugo Coder](https://github.com/luizdepra/hugo-coder)입니다. 저장소의 [MIT 라이선스](LICENSE.md)와 [기여자 목록](CONTRIBUTORS.md)을 참고하세요.
- 메뉴, 페이지 제목, GitHub, Instagram 아이콘에는 Hugo Coder에 포함된 [Font Awesome Free](https://fontawesome.com/license/free)를 사용했습니다. [웹폰트 라이선스 고지](site/themes/template/static/fonts/LICENSE.txt)와 [SCSS 라이선스 고지](site/themes/template/assets/scss/font-awesome/LICENSE.txt)를 참고하세요.
- 홈의 프로필 사진은 사이트 운영자가 제공한 여행 사진입니다. Gmail 링크에는 직접 그린 단색 아이콘을 사용했습니다.
- 소개와 활동 내용은 본인 경험을 바탕으로 작성했습니다. 본문 표현 정리와 모바일 메뉴 접근성 개선에 AI의 도움을 받았습니다.

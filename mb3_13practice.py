from mb3_13unit import TopLevelTag
from mb3_13unit import Tag
from mb3_13unit import FileHTML

if __name__=="__main__":
    with FileHTML("test.html") as fHtml_:
        with TopLevelTag("html") as html_:
            with TopLevelTag("head") as head_:
                head_.prefix = 1
                with Tag("title") as title_:
                    title_.prefix = 2
                    title_.text = "hello"
                head_.children.append(title_)
            html_.children.append(head_)
            with TopLevelTag("body") as body_:
                body_.prefix = 1
                with Tag("h1") as h1_:
                    h1_.text = "Test"
                    h1_.prefix = 2
                    h1_.attributes["class"] = "main-text"
                body_.children.append(h1_)
                with Tag("div") as div_:
                    div_.prefix = 2
                    div_.attributes["class"] = "container container-fluid"
                    div_.attributes["id"] = "lead"
                    with Tag("p") as p_:
                        p_.prefix = 3
                        p_.text = "another test"
                    div_.children.append(p_)
                    with Tag("img", is_single = True) as img_:
                        img_.prefix = 3
                        img_.attributes["src"] = "/icon.png"
                        img_.attributes["data-image"] = "responsive"
                    div_.children.append(img_)
                body_.children.append(div_)
            html_.children.append(body_)
        fHtml_.dataObj = html_
        fHtml_.write_()
    print((fHtml_.output=="screen") and "Вывод на экран" or f"Вывод в файл: {fHtml_.output}")
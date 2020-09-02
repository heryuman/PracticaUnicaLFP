#generando html
import webbrowser
def html_create(lista,tope):


    if int(tope)>0 and int(tope) <= len(lista):
        template = open("HTML/template.html", "r")
        output = open("reportepractica.html", "w")


        i = 0
        while i < int(tope):

            text = template.read().format(get_num="0", get_nombre="", get_edad="", get_activo="", get_promedio="")
            output.write(text)

            output.writelines("<tr>")
            output.writelines("<th scope = 'row'>%s</th >" % (i + 1))

            output.writelines("<td> %s </td>" % lista[i].get("nombre"))
            output.writelines("<td> %s </td>" % lista[i].get("edad"))
            output.writelines("<td> %s </td>" % lista[i].get("activo"))
            output.writelines("<td> %s </td>" % lista[i].get("promedio"))
            output.writelines("</tr>")

            i += 1
        output.writelines(" </tbody>")
        output.writelines(" </table>")
        output.writelines(" </html>")
        template.close()
        output.close()
        webbrowser.open_new_tab('reportepractica.html')
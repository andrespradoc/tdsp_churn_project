# Diccionario de datos

## Base de datos 1

**La siguiente tabla tiene los 21 columnas del dataset con su respectiva descripción y tipo de dato.

| Campo | Descripción | Tipo de dato | 
|---|---|---|
| Account Length | Duración de la cuenta | Número entero |
| Vmail Message | Cantidad de mensajes de voz | Número entero |
| Day Mins | Cantidad de Minutos de día | Número real |
| Eve Mins | Cantidad de Minutos de la tarde | Número real |
| Night Mins | Cantidad de Minutos de noche | Número real |
| Intl Mins | Cantidad de Minutos internacionales | Número real |
| CustServ Calls | Cantidad de Llamadas al servicio de atención al cliente | Número entero |
| Churn | Etiqueta si el cliente tuvo o no Cuota de abandono | Texto |
| Intl Plan | Si tiene Plan internacional | Texto |
| Vmail Plan | Si tiene Plan de correo de voz | Texto |
| Day Calls | Llamadas de día | Número entero |
| Day Charge | Cargo de llamadas de día | Número real |
| Eve Calls | Llamadas de la tarde | Número entero |
| Eve Charge | Cargo de llamadas de la tarde | Número real |
| Night Calls | Llamadas de noche | Número entero |
| Night Charge | Cargo de llamadas de noche | Número real |
| Intl Calls | Llamadas internacionales | Número entero |
| Intl Charge | Cargo de llamadas internacionales | Número real |
| State | Estado geografico| Texto |
| Area Code | Código de área | Número entero |
| Phone | Teléfono | Número de teléfono |

La base de datos consta de 3333 registros. 483 registros para los clientes con churn = 1 y 2850 para clientes con churn = 0

Los maximos y minimos de los posibles valores de las columnas se puede ver en la siguiente tabla:

|index|Account\_Length|Vmail\_Message|Day\_Mins|Eve\_Mins|Night\_Mins|Intl\_Mins|CustServ\_Calls|Day\_Calls|Day\_Charge|Eve\_Calls|Eve\_Charge|Night\_Calls|Night\_Charge|Intl\_Calls|Intl\_Charge|Area\_Code|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|count|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|3333\.0|
|mean|101\.06480648064806|8\.099009900990099|179\.77509750975094|200\.98034803480348|200\.87203720372037|10\.237293729372938|1\.5628562856285628|100\.43564356435644|30\.562307230723075|100\.11431143114311|17\.083540354035403|100\.10771077107711|9\.03932493249325|4\.4794479447944795|2\.7645814581458144|437\.18241824182417|
|std|39\.822105928595604|13\.688365372038598|54\.46738920237137|50\.713844425812|50\.57384701365836|2\.791839548408416|1\.3154910448664767|20\.069084207300897|9\.2594345539305|19\.922625293943103|4\.310667643110341|19\.568609346058558|2\.275872837660029|2\.461214270546094|0\.753772612663046|42\.371290485606615|
|min|1\.0|0\.0|0\.0|0\.0|23\.2|0\.0|0\.0|0\.0|0\.0|0\.0|0\.0|33\.0|1\.04|0\.0|0\.0|408\.0|
|25%|74\.0|0\.0|143\.7|166\.6|167\.0|8\.5|1\.0|87\.0|24\.43|87\.0|14\.16|87\.0|7\.52|3\.0|2\.3|408\.0|
|50%|101\.0|0\.0|179\.4|201\.4|201\.2|10\.3|1\.0|101\.0|30\.5|100\.0|17\.12|100\.0|9\.05|4\.0|2\.78|415\.0|
|75%|127\.0|20\.0|216\.4|235\.3|235\.3|12\.1|2\.0|114\.0|36\.79|114\.0|20\.0|113\.0|10\.59|6\.0|3\.27|510\.0|
|max|243\.0|51\.0|350\.8|363\.7|395\.0|20\.0|9\.0|165\.0|59\.64|170\.0|30\.91|175\.0|17\.77|20\.0|5\.4|510\.0|

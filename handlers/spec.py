from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.aStates import RegisterState , State
from keyboards.register_kb import SpecConfKeyBoard
import asyncio

async def speciality_kb(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data == 'Ar':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Область профессиональной деятельности выпускников:
проектирование объектов архитектурной среды;
осуществление мероприятий по реализации принятых решений;
планирование и организация процесса архитектурного проектирования.

Объекты профессиональной деятельности выпускников:
гражданские, промышленные и сельскохозяйственные здания;
интерьер гражданских и промышленных зданий;
функциональные территории и зоны городских и сельских поселений;
реставрация и реконструкция зданий;
первичные трудовые коллективы.

Виды деятельности архитекторы:
проектирование объектов архитектурной среды;
осуществление мероприятий по реализации принятых проектных решений;
планирование и организация процесса архитектурного проектирования;
выполнение работ по одной или нескольким профессиям рабочих, должностям служащих.
",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)

    elif call.data == 'Gu':
        await state.update_data(spec=call.data)
        await call.message.answer(f"область профессиональной деятельности выпускников – выполнение гидрогеологических и инженерно-геологических работ;
объектами профессиональной деятельности выпускников являются:
исследуемые территории;
полезные ископаемые;
буровые скважины и горные проходки;
транспортное, горное и буровое технологическое оборудование;
оборудование, механизмы, аппаратура и приборы для гидрогеологических и инженерно-геологических исследований;
технологические процессы буровых и горнопроходческих работ;
техническая и технологическая документация;
первичные трудовые коллективы
техник-гидрогеолог готовится к следующим видам деятельности:
ведение технологических процессов гидрогеологических и инженерно-геологических исследований при поисково-разведочных работах;
техническое обслуживание и эксплуатация оборудования, аппаратов и приборов инженерно-геологических исследований;
управление персоналом структурного подразделения;
выполнение работ по профессии «Рабочий на геологических работах»",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
        
    elif call.data == 'Pr':
        await state.update_data(spec=call.data)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(f"Студенты данной специальности учатся следующему:
Разрабатывают программные модули для ПО компьютерных систем:
Создают спецификации отдельных программных компонентов.
Пишут код программного продукта на базе готовых спецификаций, на уровне модуля.
Используют специализированные программные средства для отладки программных модулей.
Проводят тестирование программных модулей.
Оптимизируют программный код модуля.
Разрабатывают проектную и техническую документацию с использованием графических языков спецификации.

В области разработки и администрирования баз данных:
Разрабатывают объекты базы данных.
Реализуют базу данных в определенной системе управления базами данных.
Решают вопросы администрирования базы данных.
Реализуют методы и технологии защиты информации в базах данных.

При участии в интеграции программных модулей:
Анализируют проектную и техническую документацию на уровне взаимодействия программных компонентов.
Интегрируют программные модули в систему программного обеспечения.
Отлаживают программный продукт с использованием специализированного программного обеспечения.
Разрабатывают тестовые наборы и тестовые сценарии.",reply_markup= SpecConfKeyBoard())
        await state.set_state(RegisterState.cnfKbSpecState)
                
    elif call.data == 'El':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Организация и проведение работ по монтажу, сборке и демонтажу электронных приборов и устройств - выполнение сборки, монтажа и демонтажа электронных приборов и устройств, разработка технологических процессов по монтажу, и сборке электронных приборов и устройств, подбор технологического оборудования для проведения сборочно – монтажных работ.
Организация работ по выполнению настройки, регулировки и проведению испытаний электронных приборов и устройств - осуществление выбора измерительных приборов и оборудования для проведения испытаний электронных приборов и устройств, разработка технологических процессов по настройке и регулировке электронных приборов и устройств.
Организация работ по проведению технического обслуживания и ремонта электронных приборов и устройств - осуществление анализа электрических схем электронных приборов и устройств, составление алгоритмов диагностирования электронных приборов и устройств, проведение технического обслуживания и ремонта электронных приборов и устройств.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'Ra':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Область профессиональной деятельности выпускников: организация и проведение работ по монтажу, ремонту, эксплуатации и техническому обслуживанию различных видов радиоэлектронной техники.
Объекты профессиональной деятельности выпускников:
узлы и функциональные блоки различных видов изделий радиоэлектронной техники;
электрорадиоматериалы и компоненты;
технологические процессы по сборке, монтажу и наладке различных видов изделий радиоэлектронной техники;
контрольно-измерительная аппаратура;
оборудование для проведения сборочно-монтажных работ;
техническая документация;
первичные трудовые коллективы.
Квалификация выпускника базовой подготовки — техник.
Квалификация выпускника углубленной подготовки — старший техник.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'ER':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Специальность «Разработка электронных устройств и систем» подходит для тех, кто хочет изобретать новые устройства. 
        Среднее профессиональное образование дает необходимые знания и навыки для создания электронных приборов и систем. 
        Практические занятия проводятся в мастерских и лабораториях с современной аппаратурой и программным обеспечением. 
        Учебный план включает практику на профильных предприятиях. 
        Это важный элемент программы, который готовит учащихся к решению производственных и конструкторских задач. 
        Студенты изучают теоретические принципы работы электронных приборов и систем. 
        Они учатся проектировать устройства и схемы, работать с технической документацией. 
        Учащиеся осваивают производство отдельных деталей и сборку механизмов, проведение испытаний. 
        В программу включено изучение принципов установки и демонтажа электрического оборудования. 
        Студенты учатся выполнять настройку, диагностику, ремонт электронных устройств. 
        Они изучают принципы разработки софта для управления работой приборов и систем, для автоматизации процессов.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'MR':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Монтажник радиоэлектронной аппаратуры и приборов — это специалист, который:
осуществляет работу по монтажу и устройству приборов, радиоэлектронной аппаратуры;
проводит испытания приборов и готовит их к дальнейшей эксплуатации.
Монтажник радиоэлектронной аппаратуры и приборов должен уметь:
работать со сборочно-монтажными чертежами;
знать маркировку электрорадиоизделий;
выявлять и устранять неисправности в радиоэлектронной аппаратуре;
работать со схемами и специальными инструментами.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)
                        
    elif call.data == 'CK':
        await state.update_data(spec=call.data)
        await call.message.answer(f"Цифровой куратор — специалист в области компьютерной грамотности, помогающий гражданам получить навыки работы с компьютером, оргтехникой и электронными ресурсами.
Основные обязанности консультанта включают:
приём и регистрацию обращений граждан;
предоставление информации о местах и сроках проведения занятий;
подготовку презентационных материалов и компьютерного оборудования;
организацию и проведение индивидуальных консультаций и групповых мероприятий;
контроль материально-технического оснащения занятий;
оказание консультативной помощи учащимся;
проведение опросов участников об эффективности обучения.
Освоить профессию цифрового куратора можно на курсах профессиональной переподготовки. Обучение проводится дистанционно на базе уже имеющегося высшего или среднего профессионального образования.",reply_markup= SpecConfKeyBoard())
        await call.message.edit_reply_markup(reply_markup=None)
        await state.set_state(RegisterState.cnfKbSpecState)

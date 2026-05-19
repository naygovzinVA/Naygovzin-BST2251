const groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БВТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];

const rpad = (str, length) => {
    str = str.toString();
    while (str.length < length)
    str = str + ' ';
    return str
};

const printStudents = (students) => {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );

    for (let i = 0; i <= students.length - 1; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

// Функция для фильтрации студентов по группе
const filterByGroup = (students, group) => {
    return students.filter((student) => student.group === group);
};

// Функция для расчета среднего балла
const calculateAverage = (marks) => {
    const sum = marks.reduce((total, mark) => total + mark, 0);
    return sum / marks.length;
};

// Функция для фильтрации студентов по среднему баллу
const filterByAverage = (students, minAverage) => {
    return students.filter((student) => {
        const average = calculateAverage(student.marks);
        return average >= minAverage;
    });
};

console.log("Все студенты:");
printStudents(groupmates);

const groupToFilter = prompt("Введите группу для фильтрации:");
console.log("Студенты группы " + groupToFilter + ":");
const filteredByGroup = filterByGroup(groupmates, groupToFilter);
printStudents(filteredByGroup);

const minAverage = parseFloat(prompt("Введите минимальный средний балл:"));
console.log("Студенты со средним баллом выше " + minAverage + ":");
const filteredByAverage = filterByAverage(groupmates, minAverage);
printStudents(filteredByAverage);
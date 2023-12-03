document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav ul li a');
    const mainContent = document.querySelector('main');

    function handleClick(event) {
        event.preventDefault();
        mainContent.innerHTML = '';

        const linkText = event.target.textContent;

        switch (linkText) {
            case 'Institute':
                mainContent.innerHTML = '<p>The National Logistics Corporation (Urdu: نیشنل لاجسٹکس سیل; previously known as the National Logistics Cell[1]) is a Pakistani logistics company working under the overall umbrella of National Logistics Board headed by Federal Minister for Planning, Development & Special Initiatives with secretaries of relevant federal ministries as its members. It is one of the largest logistics companies in Pakistan.</p>';
                break;
            case 'Faculty':
                mainContent.innerHTML = '<ul><li><a href="#math">Math</a></li><li><a href="#compProg">Computer and Python Programming Language</a></li><li><a href="#chemMath">Chemistry and Math</a></li><li><a href="#islamiat">Islamiat</a></li><li><a href="#pakStudies">Pak Studies</a></li><li><a href="#chineseLang">Chinese Language</a></li><li><a href="#oshe">OSHE</a></li><li><a href="#electronics">Electronics</a></li></ul>';
                break;
            case 'Courses':
                mainContent.innerHTML = '<ul><li><a href="#IOTAT">IOTAT</a></li><li><a href="#MMAT">MMAT</a></li></ul>';
                break;
            case 'Activities':
                mainContent.innerHTML = '<p>Sorry, we have no activities right now. You can visit us later. Thanks!</p>';
                break;
            case 'About the Developers':
                mainContent.innerHTML = '<p>The developer name is Falak Sher, very passionate about studies and has a great attitude. Thanks for visiting this website!</p>';
                break;
            case 'Math':
                mainContent.innerHTML = '<p>Prof Hamid</p>';
                break;
            case 'Computer and Python Programming Language':
                mainContent.innerHTML = '<p>Sir Usman</p>';
                break;
            case 'Chemistry and Math':
                mainContent.innerHTML = '<p>Prof Hamid</p>';
                break;
            case 'Islamiat':
                mainContent.innerHTML = '<p>Sir Shahid Islam</p>';
                break;
            case 'Pak Studies':
                mainContent.innerHTML = '<p>Sir Abuzar</p>';
                break;
            case 'Chinese Language':
                mainContent.innerHTML = '<p>Sir Mehboob Elahi</p>';
                break;
            case 'OSHE':
                mainContent.innerHTML = '<p>Sir Quaid Khan</p>';
                break;
            case 'IOTAT':
                mainContent.innerHTML = '<p>We have 25 students currently enrolled in this course. They will go to China Jiujiang University after two years.</p>';
                break;
            case 'MMAT':
                mainContent.innerHTML = '<p>We have 25 students enrolled in MMAT. These students will also go to China after completing two years of studies in Pakistan.</p>';
                break;
            default:
                break;
        }
    }

    navLinks.forEach(function(link) {
        link.addEventListener('click', handleClick);
    });
});

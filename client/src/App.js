import logo from "./logo.svg";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import { NavigationBar } from "./components/NavigationBar";
import { Home } from "./pages/Home";
import { About } from "./pages/About";
import "./components/styles.css"

function App() {
  return (
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, minimal-ui" />
      <link rel="stylesheet" href="styles.css"></link>
    </head>
    
    <body id="body-tag">
      <header class="coursearch-masthead">
        <div class="coursearch-masthead-branding">
          <a href="/phpbin/course-search/">Boston University <span>Course Search 2.0</span></a>
        </div>
      </header>
    
      <main class="coursearch-main">
            <header class="coursearch-header">
          <p>Search our database of over 7,000 courses.</p>
        </header>
    
        <p>Perform a basic search by entering keywords you would expect to find in the course description or by entering a full course number (example: CAS XX 123).  If you would like to see expected course offerings for a particular semester, select that semester in the drop-down box. If you would like to see all courses expected to be offered in the future, select “Future Semesters.”</p>
        <p>To perform a more targeted search, select Additional Search Options</p>
      
        <div class="coursearch-searchfields">
          <input type="hidden" name="page" id="page" value="w0" />
          <input type="hidden" name="pagesize" id="pagesize" value="10" />
          <input type="hidden" name="adv" id="adv" value="1" />
          <input type="hidden" name="nolog" id="nolog" value="" />
    
            <label class="searchbar">
              Keyword or Full Course Number (example: CAS XX 123) 
              <input class="coursearch-searchfields-keyword-field" type="search" name="search_adv_all" value=""></input>
            </label>
    
            <label class="dropdown" >
              Semester
              <select class="coursearch-searchfields-semester-select" name="yearsem_adv">
                <option value="2023-SPRG" selected="selected" >Spring 2023</option>
                <option value="*"  >Future Semesters</option>
              </select>
            </label>
    
            <span>
              <button id="search-submit" type="submit" class="coursearch-searchfields-submit">Search</button>
            </span>
        </div>
    
        <div class="additional-info">
          <button class="coursearch-options-expand" type="button" data-selection-count="" ><strong>^</strong> Additional Search Options</button>
        </div>
      </main>
    
      <footer class="coursearch-footer">
        <ul class="coursearch-footer-links">
          <li><a href="https://www.bu.edu/academics/bulletin/">Bulletin</a></li>
    
          <li><a href="https://www.bu.edu/link/bin/uiscgi_studentlink.pl/uismpl/?ModuleName=menu.pl&NewMenu=Home">Student Link</a></li>
    
          <li><a href="http://www.bu.edu/help/tech/">Contact</a></li>
    
          <li><a href="https://www.bu.edu/advising/">Undergraduate Advising</a></li>
        </ul>
    
        <div class="coursearch-footer-copyright">
          <p>© 2022 Boston University Course Search 2.0</p>
        </div>
    
        <div class="coursearch-footer-branding">
          <a class="coursearch-footer-masterplate" href="https://www.bu.edu">
            <img src="/client/public/bu.ico"></img>
          </a>
        </div>
      </footer>
    </body>
    </html>    
  );
}

export default App;

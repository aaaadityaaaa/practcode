var SideNavToggle = false
var PractcodeSideNav = document.getElementById("PractcodeSideNavid")
var PractcodeSidebar_userstatusid = document.getElementById("PractcodeSidebar_userstatusid")


const PractcodetoggleSidenav = () =>{
    
    if(SideNavToggle){
        PractcodeSideNav.classList.remove('activeSidenav')
        PractcodeSidebar_userstatusid.classList.remove('activeuser')
        document.getElementById("PractcodeMainRootid").classList.remove('activeSidenav')
        SideNavToggle = false
    }else{
        PractcodeSideNav.classList.add('activeSidenav')
        PractcodeSidebar_userstatusid.classList.add('activeuser')
        document.getElementById("PractcodeMainRootid").classList.add('activeSidenav')
        SideNavToggle = true
    }
}



$(document).ready(function() {
    $('#dropdown-button').click(function() {
      $('#dropdown-content').slideToggle(100);
    });
  });
function varargout = Robot(varargin)
% ROBOT MATLAB code for Robot.fig
%      ROBOT, by itself, creates a new ROBOT or raises the existing
%      singleton*.
%
%      H = ROBOT returns the handle to a new ROBOT or the handle to
%      the existing singleton*.
%
%      ROBOT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ROBOT.M with the given input arguments.
%
%      ROBOT('Property','Value',...) creates a new ROBOT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Robot_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Robot_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Robot

% Last Modified by GUIDE v2.5 07-May-2020 17:37:15

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Robot_OpeningFcn, ...
                   'gui_OutputFcn',  @Robot_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Robot is made visible.
function Robot_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Robot (see VARARGIN)

% Choose default command line output for Robot
handles.output = hObject;


% create an axes that spans the whole gui
ah = axes('unit', 'normalized', 'position', [0 0 1 1]); 
% import the background image and show it on the axes
bg = imread('raghad3.jpg'); imagesc(bg);
% prevent plotting over the background and turn the axis off
set(ah,'handlevisibility','off','visible','off')
% making sure the background is behind all the other uicontrols
uistack(ah, 'bottom');
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Robot wait for user response (see UIRESUME)
% uiwait(handles.figure1);



% --- Outputs from this function are returned to the command line.
function varargout = Robot_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function Th_1_Callback(hObject, eventdata, handles)
% hObject    handle to Th_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th_1 as text
%        str2double(get(hObject,'String')) returns contents of Th_1 as a double


% --- Executes during object creation, after setting all properties.
function Th_1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Th_2_Callback(hObject, eventdata, handles)
% hObject    handle to Th_2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th_2 as text
%        str2double(get(hObject,'String')) returns contents of Th_2 as a double


% --- Executes during object creation, after setting all properties.
function Th_2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th_2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function D_1_Callback(hObject, eventdata, handles)
% hObject    handle to D_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of D_1 as text
%        str2double(get(hObject,'String')) returns contents of D_1 as a double


% --- Executes during object creation, after setting all properties.
function D_1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to D_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Theta_1 = str2double(get(handles.Th_1,'String'))*pi/180;
if Theta_1>(37*pi/45)
    Theta_1=37*pi/45;
else if Theta_1<(-37*pi/45)
        Theta_1=-37*pi/45;
    end
end
Theta_2 = str2double(get(handles.Th_2,'String'))*pi/180;
if Theta_2>(5*pi/6)
    Theta_2=5*pi/6;
else if Theta_2<(-5*pi/6)
        Theta_1=-5*pi/6;
    end
end
D = str2double(get(handles.D_1,'String'));
if D>.21
    D=.21;
end
L_1 = .35;
L_2 = .3;
d_1=.175;
d_4=.015;
Theta_3 = str2double(get(handles.Th_3,'String'))*pi/180;

L(1)=Link([0 .175 L_1 0 0]);
L(2)=Link([0 0 L_2 pi 0]);
L(3)=Link([0 0 0 0 1]);
L(4)=Link([0 .015 0 0 0]);



Robot = SerialLink(L);
Robot.name = 'LAB_8';

%Robot.plot([Theta_1 Theta_2 0]);
%T = Robot.fkine([Theta_1 Theta_2 D Theta_3]);


A1=[( cos(Theta_1)),(-1* sin(Theta_1)),0,(L_1* cos(Theta_1));
    ( sin(Theta_1)),( cos(Theta_1))   ,0,(L_1* sin(Theta_1));
    0,0,1,d_1;
    0,0,0,1 ];

A2= [( cos(Theta_2)),( sin(Theta_2))   ,0,(L_2* cos(Theta_2)) ;
     ( sin(Theta_2)),(-1* cos(Theta_2)),0,(L_2* sin(Theta_2)) ;
     0,0,-1,0;
     0,0,0,1 ];
              
A3= [1, 0, 0,0 ;
     0, 1, 0,0 ;
     0, 0, 1,D;
     0, 0, 0,1 ];
 A4= [( cos(Theta_3)),(-1* sin(Theta_3)),0,0 ;
     ( sin(Theta_3)),( cos(Theta_3))   ,0,0 ;
     0,0,1,d_4;
     0,0,0,1 ];

T= A1*A2*A3*A4;

 for th1=0:.1:Theta_1
 Robot.plot([th1 0 D 0]);
 pause(.25);
 end
 for th2=0:.1:Theta_2
 Robot.plot([Theta_1 th2 D 0]);
 pause(.25);
 end
 
%  for d=0:.05:D
%      Robot.plot([Theta_1 Theta_2 d 0]);
%  pause(.25);
%  end
 
 for th3=0:.1:Theta_3
 Robot.plot([Theta_1 Theta_2 D th3]);
 pause(.25);
 end
 
 
 
 Robot.plot([Theta_1 Theta_2 D Theta_3]);


set(handles.text1,'String' ,double(T(1,4)));
set(handles.text2,'String' , double(T(2,4)));
set(handles.text3,'String' , double(T(3,4)));

set(handles.text13,'String' ,double(T(1,1)));
set(handles.text14,'String' , double(T(1,2)));
set(handles.text15,'String' , double(T(1,3)));

set(handles.text17,'String' ,double(T(2,1)));
set(handles.text18,'String' , double(T(2,2)));
set(handles.text19,'String' , double(T(2,3)));

set(handles.text21,'String' ,double(T(3,1)));
set(handles.text22,'String' , double(T(3,2)));
set(handles.text23,'String' , double(T(3,3)));



function Th_3_Callback(hObject, eventdata, handles)
% hObject    handle to Th_3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th_3 as text
%        str2double(get(hObject,'String')) returns contents of Th_3 as a double


% --- Executes during object creation, after setting all properties.
function Th_3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th_3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

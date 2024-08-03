% Parametri
g = 9.81;           % ubrzanje sile teže
v0 = 20;            % početna brzina lopte
theta = pi/4;       % kut izbačaja
alpha = 0;          % otpor zraka
T = 5
interval=[0,T]      % maksimalna duljina vremenskog intervala


% Početni uvjeti
x1=0;		% Vrijednost prve komponente pocetnog polozaja
x2=0;		% Vrijednost druge komponente pocetnog polozaja
v1=v0 * cos(theta);		% Vrijednost prve komponente pocetne brzine
v2=v0 * sin(theta);		% Vrijednost druge komponente pocetne brzine
uvjeti=[x1 x2 v1 v2]


% Desne strane sustava
F = @(t, y) [y(3); y(4);-alpha*y(2) ; -alpha*y(4) - g];

% Definicija funkcije za događaj - zelim da integriranje stane kad y
%promijeni predznak, tj ne zelim ocrtavane grafa za negativne vrijednosti
function [value, isterminal, direction] = stopEvent(t, y)
    value = y(2);              % Pratimo vertikalnu poziciju y(2)
    isterminal = 1;            % Zaustavljamo integraciju kad se događaj ostvari
    direction = -1;            % Tražimo da y(2) bude manje ili jednako nuli
end

opts = odeset('RelTol', 1e-7, 'Events', @stopEvent);
[t,y]=ode45(F,interval,uvjeti,opts);


% Plotanje rezultata
plot(y(:,1), y(:,2), 'LineWidth', 2);
xlabel('x');
ylabel('y');
grid on;



% Parametri
g = 9.81;           % ubrzanje sile teže
v0 = 20;            % početna brzina lopte
theta = pi/4;       % kut izbačaja
alpha = 0.5;          % otpor zraka
T = 5
interval=[0,T]      % maksimalna duljina vremenskog intervala


% Početni uvjeti
x1=0;		% Vrijednost prve komponente pocetnog polozaja
x2=0;		% Vrijednost druge komponente pocetnog polozaja
v1=v0 * cos(theta);		% Vrijednost prve komponente pocetne brzine
v2=v0 * sin(theta);		% Vrijednost druge komponente pocetne brzine
uvjeti=[x1 x2 v1 v2]


% Desne strane sustava
F = @(t, y) [y(3); y(4);-alpha*y(3) ; -alpha*y(4) - g];

function [value, isterminal, direction] = najvisa_tocka(t, y)
    value = y(4);              % Pratimo vertikalnu poziciju y(2)
    isterminal = 1;            % Zaustavljamo integraciju kad se događaj ostvari
    direction = -1;            % Promatramo slucajeve samo kad se vrijednost
                               %y(1) smanjuje (1 znaci da
                               %bismo trazili da se vrijednost y(1) povecava, a 0 znaci da nema restrikcija)
end

opts = odeset('RelTol', 1e-11, 'Events', @najvisa_tocka);
[t,y,tevent, yevent, ie]=ode45(F,interval,uvjeti,opts);
% Ispis točke gdje se događaj dogodio
fprintf('Najviša točka putanje postiže se u (x, y) = (%.10f, %.10f)\n', yevent(1, 1), yevent(1, 2));

% Plotanje rezultata
plot(y(:,1), y(:,2), 'LineWidth', 2);
xlabel('x');
ylabel('y');
grid on;


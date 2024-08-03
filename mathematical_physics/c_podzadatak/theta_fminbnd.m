% Parametri
g = 9.81;           % ubrzanje sile teže
v0 = 20;            % početna brzina lopte
alpha = 0.2;          % otpor zraka
T = 5               % maksimalna duljina vremenskog intervala
interval=[0,T]
xB = 11.8475917655  %x koordinata od B
yB =  6.9851731350  %y koordinata od B




function d = solution(theta,alpha,g,v0)
       % Parametri
       g = 9.81;           % ubrzanje sile teže
       v0 = 20;            % početna brzina lopte
       alpha = 0.2;          % otpor zraka
       T = 5               % maksimalna duljina vremenskog intervala
       interval=[0,T]
       xB = 11.8475917655  %x koordinata od B
       yB =  6.9851731350  %y koordinata od B


        % Početni uvjeti
        uvjeti = [0, 0, v0 * cos(theta), v0 * sin(theta)];

        % Desne strane sustava ODE
        F = @(t, y) [y(3); y(4); -alpha * y(3); -alpha * y(4) - g];

        % Rješavanje sustava ODE
        [t, y] = ode45(F, interval, uvjeti);

        % Izračunavanje udaljenosti do točke B
        distances = sqrt((y(:, 1) - xB).^2 + (y(:, 2) - yB).^2);
        d = min(distances);
    end

     % Traženje optimalnog kuta koristeći fminbnd
    F=@(theta)[-solution(theta,alpha,g,v0)];
    Optimalantheta = fminbnd(F,0.01,pi/2-0.01)
    disp(Optimalantheta)

%problem je sto fminbnd vraca samo jednu vrijednost tako da nemogu pronaci
%sva rjesenja, nije najbolje rjesenje


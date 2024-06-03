function flaviaWriter()

fid = fopen('test.res','w');

fprintf(2,'* %s\n','Creating flavia.res from FEA. THIS MAY TAKE A FEW MINUTES ...')

nodes = load('nodesInfo.dat');
elems = load('elementsInfo.dat');
solidElts = elems(:,1);

fprintf(fid,'GiD Post Results File 1.0 \n\n');

%----------------------DISPLACEMENTS----------------------------------

displacements = load('displacement.out');

allTimes = displacements(:,1);
displacements(:,1) = [];

[numSteps,numDisps] = size(displacements);
numNodes = numDisps/3;

for i = 1:numSteps
	fprintf(fid,'Result "a.  Nodal Displacements" "Loading_Analysis"\t%12.5g Vector OnNodes\n', allTimes(i));
	fprintf(fid,'ComponentNames "X-Displacement"  "Y-Displacement" "Z-Displacement" \n');
	fprintf(fid,'Values\n');

	u = reshape( displacements(i,:), 3, numNodes );
	for j=1:numNodes
		fprintf(fid,'%d \t %-12.8e %-12.8e %-12.8e \n', j, u(:,j));
	end
	fprintf(fid,'End Values \n') ;
	fprintf(fid,' \n') ;
end

clear displacements

fprintf(2,'* %s\n','Done with displacements ...')

%----------------------PORE PRESSURES----------------------------------

porePress = load('porePressure.out');

allTimes = porePress(:,1);
porePress(:,1) = [];

[numSteps,numNodes] = size(porePress);
ppRatio = zeros(numSteps,numNodes);

iniPress = reshape(porePress(1,:), 1, numNodes);

for i = 1:numSteps
	fprintf(fid,'Result "a.  Nodal PorePressure" "Loading_Analysis"\t%12.5g Scalar OnNodes\n', allTimes(i));
	fprintf(fid,'ComponentNames "PorePressure" \n');
	fprintf(fid,'Values\n');

	u = reshape( porePress(i,:), 1, numNodes );
	exPWP(i,:) = abs(u - iniPress);
	for j=1:numNodes
		fprintf(fid,'%d \t %-12.8e \n', j, u(:,j));
	end
	fprintf(fid,'End Values \n') ;
	fprintf(fid,' \n') ;
end

fprintf(2,'* %s\n','Done with porepressure ...')

%------------------------STRESSES-------------------------------------

%stress = load('stress.out');
%stress(:,1) = [];

%[nStep,nStress] = size(stress);
%nElem = nStress/7;

% load and combine data
for i = 1:8
    mLoad = sprintf('pstress{i} = load(''stress%i.out'');',i);
    eval(mLoad)
    if i == 1
        ptime = pstress{i}(:,1);
    end
    pstress{i}(:,1) = [];
    stress{i} = [pstress{i}];
end
clear pstress

time = [ptime];

[nStep,nStress] = size(stress{1});
nElem = nStress/7

gp = cell(8, 1);
for k = 1:nStep
  fprintf(fid,'GaussPoints "stress" ElemType Hexahedra\n');
	fprintf(fid,'Number of Gauss Points: 8\n');
  %fprintf(fid,'Nodes: Included\n');
	fprintf(fid,'Natural Coordinate: Internal\n');
	fprintf(fid,'End Gausspoints\n\n');
	fprintf(fid,'Result "Gauss Point Stress" "Loading_Analysis"\t%12.5g', allTimes(k));
    %fprintf(fid,'\tMatrix OnGaussPoints "stress"\n');
    fprintf(fid,'\tMatrix OnGaussPoints  GP_HEXAHEDRA_8 \n');
	fprintf(fid,'Values\n');

  for i = 1:8
        gp{i} = reshape(stress{i}(k,:), 7, nElem);
    end

    for j = 1:nElem
    fprintf(fid,'%6.0f  ', j);
      for i = 1:8
            jn = 1;
            fprintf(fid,'%12.6g %12.6g %12.6g %12.6g %12.6g %12.6g\n', gp{i}(1,jn), gp{i}(2,jn), gp{i}(3,jn), gp{i}(4,jn), gp{i}(5,jn), gp{i}(6,jn));

	    end
    end
	fprintf(fid,'End Values \n');
	fprintf(fid,'\n');
end



%    gp = reshape(stress(k,:), 7, nElem);

%    for j = 1:nElem
%		eleID = solidElts(j,1);
%        fprintf(fid,'%6.0f  ', eleID);
%		fprintf(fid,'%12.6g %12.6g %12.6g %12.6g %12.6g %12.6g \n', gp(1:6,j));
%	end
%	fprintf(fid,'End Values \n');
%	fprintf(fid,'\n');
%end

clear stress gp

fprintf(2,'* %s\n','Done with stress ...')

%------------------------STRAIN-------------------------------------

%stress = load('stress.out');
%stress(:,1) = [];

%[nStep,nStress] = size(stress);
%nElem = nStress/7;

% load and combine data
for i = 1:8
    mLoad = sprintf('pstrain{i} = load(''strain%i.out'');',i);
    eval(mLoad)
    if i == 1
        ptime = pstrain{i}(:,1);
    end
    pstrain{i}(:,1) = [];
    strain{i} = [pstrain{i}];
end
clear pstrain

time = [ptime];

[nStep,nStrain] = size(strain{1});
nElem = nStrain/6

gp = cell(8, 1);
for k = 1:nStep
  fprintf(fid,'GaussPoints "strain" ElemType Hexahedra\n');
	fprintf(fid,'Number of Gauss Points: 8\n');
  %fprintf(fid,'Nodes: Included\n');
	fprintf(fid,'Natural Coordinate: Internal\n');
	fprintf(fid,'End Gausspoints\n\n');
	fprintf(fid,'Result "Gauss Point Strains" "Loading_Analysis"\t%12.5g', allTimes(k));
    %fprintf(fid,'\tMatrix OnGaussPoints "stress"\n');
    fprintf(fid,'\tMatrix OnGaussPoints  GP_HEXAHEDRA_8 \n');
	fprintf(fid,'Values\n');

  for i = 1:8
        gp{i} = reshape(strain{i}(k,:), 6, nElem);
    end

    for j = 1:nElem
    fprintf(fid,'%6.0f  ', j);
      for i = 1:8
            jn = 1;
            fprintf(fid,'%12.6g %12.6g %12.6g %12.6g %12.6g %12.6g\n', gp{i}(1,jn), gp{i}(2,jn), gp{i}(3,jn), gp{i}(4,jn), gp{i}(5,jn), gp{i}(6,jn));

	    end
    end
	fprintf(fid,'End Values \n');
	fprintf(fid,'\n');
end



%    gp = reshape(stress(k,:), 7, nElem);

%    for j = 1:nElem
%		eleID = solidElts(j,1);
%        fprintf(fid,'%6.0f  ', eleID);
%		fprintf(fid,'%12.6g %12.6g %12.6g %12.6g %12.6g %12.6g \n', gp(1:6,j));
%	end
%	fprintf(fid,'End Values \n');
%	fprintf(fid,'\n');
%end

clear stress gp

fprintf(2,'* %s\n','Done with strain ...')


%----------------------END OF RESULT FILE ----------------------------------
fclose(fid);

return

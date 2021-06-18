"""
Function translated automatically using 'matlab.to.r()'

Author: Caiya Zhang, Yuchen Zheng
"""
##!!!!f

from numpy import ndarray
from project.zeros import zeros

from project.feval import do_call

def grad_all (func, select_par, nRow, *args, subset=None, currentOcc=None, noPopED=False, offdiag=False):
    
    for arg in args:
        for i in range(len(args)):
            arg_list = []
            arg_list[i] = arg
    def0 = arg_list[[select_par]]
    
    if currentOcc is None:

        idx = idx0 = seq_along(def0)
        if subset != None:
            idx0 = as.vector(cumsum(subset)*subset)
            idx = seq(max(idx0))
    
        if def0 is ndarray and select_par > 6 and offdiag == False:
            idx0 = diag(idx0)
    
        if is.matrix(def0) and select_par>6 and offdiag == True:
            tmp = 0*def0
            tmp[lower.tri(tmp)] = idx0
            idx0 = tmp + t(tmp)
    
    else:
        idx  = seq(size(def0,1))
        idx0 = zeros(size(def0))
        idx0[,currentOcc] = idx
  

    poped_db = arg_list[[len(arg_list)]]
    hlf  = poped_db["settings"]["hlf"]
    grad_all_switch = poped_db["settings"]["grad_all_switch"][1]

    if noPopED == True: 
      arg_list = arg_list[-len(arg_list)]
  
    gradX = zeros(nRow, length(idx))

    #Central approximation
    if grad_all_switch == 1:
        for i in idx:
            arg_list[[select_par]] = def0 + (idx0 == i)*hlf
            def_plus <- do_call(func, arg_list)
            arg_list[[select_par]] = def0 - (idx0 == i)*hlf
            def_minus <- do_call(func, arg_list)
            if noPopED == False:
                def_plus = def_plus[[1]]        
                def_minus = def_minus[[1]]        
            gradX[,i] = (def_plus - def_minus)/(2.0*hlf)
    
    else:
    #Complex approximation
        if grad_all_switch == 0:
            for i in idx:
                arg_list[[select_par]] = def0 + (idx0 == i) * complex(real = 0, imaginary = hlf)
                def_plus = do_call(func, arg_list)[[1]]
                gradX[,i] = Im(def_plus) / hlf
        else:
            raise Exception("Unknown derivative option for grad_all")

    return gradX
   